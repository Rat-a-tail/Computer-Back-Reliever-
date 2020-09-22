#### Solutions to Practice Problems for Day 14 ####

import cImage as image

# Problem 1:
def convertBlackWhite(input_image):
    new_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())

    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            p = input_image.getPixel(col, row) # get the pixel's current colors

            if(p.getRed() + p.getGreen() + p.getBlue() < 383): # if total is less than 383, set to black
                newpixel = image.Pixel(0, 0, 0)
                new_image.setPixel(col, row, newpixel)
            else: # otherwise total is greater than 383, set to white
                newpixel = image.Pixel(255, 255, 255)
                new_image.setPixel(col, row, newpixel)

    return new_image



# Problem 2:
def halfSize(input_image):
    new_image = image.EmptyImage(input_image.getWidth()//2, input_image.getHeight()//2)
    for col in range(new_image.getWidth()):
        for row in range(new_image.getHeight()):
            p = input_image.getPixel(col*2, row*2) # need to skip every other pixel
            new_image.setPixel(col, row, p)

    return new_image



# Problem 3:
def blur(input_image):
    new_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())

    #loop over all pixels in input_image
    for col in range(1, input_image.getWidth()-1):
        for row in range(1, input_image.getHeight()-1):
            #get this pixel and its neighbors
            pixel = input_image.getPixel(col, row)
            left = input_image.getPixel(col-1, row)
            right = input_image.getPixel(col+1, row)
            up = input_image.getPixel(col, row-1)
            down = input_image.getPixel(col, row+1)

            #compute the new color components
            new_r = int((pixel.getRed() + left.getRed() + right.getRed() + up.getRed() + down.getRed())/5)
            new_g = int((pixel.getGreen() + left.getGreen() + right.getGreen() + up.getGreen() + down.getGreen())/5)
            new_b = int((pixel.getBlue() + left.getBlue() + right.getBlue() + up.getBlue() + down.getBlue())/5)

            #set the pixel in the new image
            new_pixel = image.Pixel(new_r, new_g, new_b)
            new_image.setPixel(col, row, new_pixel)

    return new_image



#testing: modify this to test the solutions above
def main():
    win = image.ImageWin()
    img = image.Image("kitten1.gif")
    
    img.draw(win)
    
    bw_img = convertBlackWhite(img)
    bw_img.setPosition(img.getWidth()+10,0)
    bw_img.draw(win)
    
    half_img = halfSize(img)
    half_img.setPosition(0, img.getHeight()+10)
    half_img.draw(win)
    
    blur_img = blur(img)
    blur_img.setPosition(img.getWidth()+10, img.getHeight()+10)
    blur_img.draw(win)
    
    win.exitonclick()

if __name__ == "__main__":
    main()
