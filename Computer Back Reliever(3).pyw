import tkinter as tk

# Created classes for each drop down menu with each option and their value in a dictionary
class Book:    
    def __init__(self,books):  
        self.book_s ={'STEM Textbook': 6,'Small Novel':0.75, 'Large Novel':2, 'Notebook':1, 'Books':0, 'None':0}
        self.books=books
    def gettype_of_book(self):
        return self.book_s[self.books]
   
class Laptop:
    def __init__(self,model):
        self.model_w={'Computer':0, 'Macbook Pro':3.02,'None':0, 'Dell Inspiron':5.11, 'Lenovo': 4.2, 'Asus':1.87 ,'Acer': 7.5 ,'Microsoft Pro':1.69 ,'Toshiba Radius':4.96, 'Samsung':1.8}
        self.model=model
    def getWeight(self):
        return self.model_w[self.model]

class Miscellaneous:
    def __init__(self, weight):
        self.weight_m ={'Miscellaneous':0, 'Small':1, 'None':0, 'Medium':1.5,'Large':2}
        self.weight = weight
    def getweight_m(self):
        return self.weight_m[self.weight]

# Created a class for the tkinter window and how it's arranged
class program:
    def __init__(self):
        self.book = ' '
        self.laptop = ' '
        self.misc = ' '
        self.bagWeight = 0
        self.userWeight = 0
        self.calculation = ' '
        self.boxcolor = 'white'
        
        self.window= tk.Tk()
        self.window.title("Computer Back Reliever")
        self.window.configure(bg="Ivory")
        self.Width = 500
        self.Height = 300
        self.myCanvas = tk.Canvas(self.window,width = self.Width, height = self.Height, bg="MintCream")

        #Set drop down menu default value to the category name
        self.v1 = tk.StringVar(self.window)
        self.v1.set("Books") # default value
        
        self.v2 = tk.StringVar(self.window)
        self.v2.set("Computer") # default value

        self.v3 = tk.StringVar(self.window)
        self.v3.set("Miscellaneous") # default value

        #Created TK Canvases to allow for easy rearranging of sections of the window, and to allow for multiple lables and entrys next to each other
        
        #This Canvas is the small space we see between the first drop down menu and the top of the window
        self.S = tk.Canvas(self.window)
        self.S.pack()
        self.space1 = tk.Label(self.S, text=" ", bg="Ivory")
        self.space1.pack()

        #Create Canvas for instruction 1
        self.i1 = tk.Canvas(self.window)
        self.i1.pack()
        self.instruct1 = tk.Label(self.i1, text="Please input your weight, in pounds, as a whole number", font=("Courier", 16))
        self.instruct1.pack(side=tk.LEFT)

        #Canvas for the User's weight Entry
        self.E = tk.Canvas(self.window)
        self.E.pack()

        self.we1 = tk.Label(self.E, text="User Weight: ", font=("Courier", 15))
        self.we1.pack(side=tk.LEFT)

        self.S2 = tk.Canvas(self.window)
        self.S2.pack()
        self.space2 = tk.Label(self.S2, text=" ", bg="Ivory")
        self.space2.pack()

        self.i2 = tk.Canvas(self.window)
        self.i2.pack()
        self.instruct2 = tk.Label(self.i2, text="Select the amount of books in your bag or an equal amount of book weight.", font=("Courier", 16))
        self.instruct2.pack(side=tk.LEFT)
        
        self.i3 = tk.Canvas(self.window)
        self.i3.pack()
        self.instruct3 = tk.Label(self.i3, text="A STEM textbook is 6 pounds, a Small Novel is 0.75, a Large Novel is 2, and a Notebook is 1.", font=("Courier", 15))
        self.instruct3.pack(side=tk.LEFT)
        
        #Use StringVar throughout the code so the label is dynamic depending on the calculations
        self.we2var = tk.StringVar()
        self.we2var.set("0")
        self.we2 = tk.Entry(self.E, textvariable=self.we2var, width=3)
        self.we2.pack(side=tk.LEFT)

        #Canvases for each drop down menu, labels and entry multipliers
        self.A1 = tk.Canvas(self.window)
        self.S3 = tk.Canvas(self.window)
        self.i5 = tk.Canvas(self.window)
        self.A2 = tk.Canvas(self.window)
        self.S4 = tk.Canvas(self.window)
        self.i4 = tk.Canvas(self.window)
        self.i6 = tk.Canvas(self.window)
        self.A3 = tk.Canvas(self.window)
        self.S5 = tk.Canvas(self.window)

        self.A1.pack()
        self.S3.pack()
        self.i5.pack()
        self.A2.pack()
        self.S4.pack()
        self.i4.pack()
        self.i6.pack()
        self.A3.pack()
        self.S5.pack()

        self.entry1var = tk.StringVar()
        self.entry2var = tk.StringVar()
        self.entry3var = tk.StringVar()

        #Default multiplier to 1
        self.entry1var.set("1")
        self.entry2var.set("1")
        self.entry3var.set("1")
        
        #Made sure to add each multiplier to their respective Canvas
        self.entry1 = tk.Entry(self.A1, width=3, textvariable=self.entry1var)
        self.space3 = tk.Label(self.S3, text=" ", bg="Ivory")
        self.instruct5 = tk.Label(self.i5, text="Select the type of computer in your bag.", font=("Courier", 16))
        self.entry2 = tk.Entry(self.A2, width=3, textvariable=self.entry2var)
        self.space4 = tk.Label(self.S4, text=" ", bg="Ivory")
        self.instruct4 = tk.Label(self.i4, text="Select the amount of miscellaneous items, or an equal weight.", font=("Courier", 16))
        self.instruct6 = tk.Label(self.i6, text="Small items are 1 pound, Medium are 1.5, and Large are 2.", font=("Courier", 15))
        self.entry3 = tk.Entry(self.A3, width=3, textvariable=self.entry3var)
        self.space5 = tk.Label(self.S5, text=" ", bg="Ivory")

        #Pack each part of the Canvas to the left so that they appear in order from left to right
        self.entry1.pack(side=tk.LEFT)
        self.space3.pack()
        self.instruct5.pack(side=tk.LEFT)
        self.entry2.pack(side=tk.LEFT)
        self.space4.pack()
        self.instruct4.pack(side=tk.LEFT)
        self.instruct6.pack(side=tk.LEFT)
        self.entry3.pack(side=tk.LEFT)
        self.space5.pack()

        self.multsym1 = tk.Label(self.A1, text=" X ", font="Courier")
        self.multsym2 = tk.Label(self.A2, text=" X ", font="Courier")
        self.multsym3 = tk.Label(self.A3, text=" X ", font="Courier")

        self.multsym1.pack(side=tk.LEFT)
        self.multsym2.pack(side=tk.LEFT)
        self.multsym3.pack(side=tk.LEFT)

        #Add each drop down menu to their respective Canvas
        self.w = tk.OptionMenu(self.A1, self.v1, "Books", "STEM Textbook", "Small Novel", "Large Novel", "Notebook", "None")
        self.w.config(font=("Courier", 15))
        self.ww = tk.OptionMenu(self.A2, self.v2, "Computer", "Macbook Pro", "Dell Inspiron","Lenovo","Asus","Acer","Microsoft Pro","Toshiba Radius","Samsung", "None")
        self.ww.config(font=("Courier", 15))
        self.www = tk.OptionMenu(self.A3, self.v3, "Miscellaneous", "Small", "Medium", "Large", "None")
        self.www.config(font=("Courier", 15))

        self.w.pack(side=tk.LEFT)
        self.ww.pack(side=tk.LEFT)
        self.www.pack(side=tk.LEFT)

        self.eq1 = tk.Label(self.A1, text=" = ", font="Courier")
        self.eq2 = tk.Label(self.A2, text=" = ", font="Courier")
        self.eq3 = tk.Label(self.A3, text=" = ", font="Courier")

        self.eq1.pack(side=tk.LEFT)
        self.eq2.pack(side=tk.LEFT)
        self.eq3.pack(side=tk.LEFT)
        
        #Create another StringVar to make the Total calculation dynamic
        self.totaldis1var = tk.StringVar()
        self.totaldis2var = tk.StringVar()
        self.totaldis3var = tk.StringVar()

        self.totaldis1 = tk.Label(self.A1, textvariable=self.totaldis1var)
        self.totaldis2 = tk.Label(self.A2, textvariable=self.totaldis2var)
        self.totaldis3 = tk.Label(self.A3, textvariable=self.totaldis3var)

        self.totaldis1.pack(side=tk.LEFT)
        self.totaldis2.pack(side=tk.LEFT)
        self.totaldis3.pack(side=tk.LEFT)
        
        #Create another Canvas for the total compute button and the display of the total bag weight
        self.B = tk.Canvas(self.window)
        self.B.pack()

        self.calculateButton = tk.Button(self.B,text = "Compute",command = self.bagCalc, width=12, font=("Courier", 22))
        self.calculateButton.pack(side=tk.LEFT)

        self.TOTlabel1 = tk.Label(self.B, text=" Total: ", font=("Courier", 16))
        self.TOTlabel1.pack(side=tk.LEFT)

        self.TOTlabel2var = tk.StringVar()
        self.TOTlabel2 = tk.Label(self.B, textvariable=self.TOTlabel2var)
        self.TOTlabel2.pack(side=tk.LEFT)

        #Create rectangle with dynamic color background
        self.rectangle = self.myCanvas.create_rectangle(self.Width//2 - 150, self.Height//2 -50, self.Width//2 + 150, self.Height//2 + 50, fill = self.boxcolor,width=1,outline = "black")
        self.myCanvas.pack()

        #Create a second rectangle to overlay to display text relating to the color
        self.rectangle2var = tk.StringVar()
        self.rectangle2 = tk.Label(self.myCanvas, textvariable=self.rectangle2var, bg="DarkSlateGray", fg="white", font=("Courier", 15))
        self.rectangle2.place(x=(self.Width//2 - 150), y=(self.Height//2 -50))
        self.myCanvas.pack()

        #Configure width of drop down menu size
        self.w.configure(width=14)
        self.ww.configure(width=14)
        self.www.configure(width=14)

        self.quitButton=tk.Button(self.window,text="Quit", font=("Courier", 20))
        self.quitButton.pack()
        self.quitButton['command'] = self.window.destroy

    #Calculate the bag weight in relation to the User's weight
    def bagCalc(self):
        self.book = Book(self.v1.get())
        self.laptop = Laptop(self.v2.get())
        self.misc = Miscellaneous(self.v3.get())

        self.mul1 = 1
        self.mul2 = 1
        self.mul3 = 1

        #Make the multipliers bug-proof and prevent anything besides an integer from working in the code, allowing the program to still pass
        try: self.mul1 = int(self.entry1var.get())
        except: pass
        try: self.mul2 = int(self.entry2var.get())
        except: pass
        try: self.mul3 = int(self.entry3var.get())
        except: pass

        #Calculate the multipliers for each category and edit the labels using StringVar
        self.weight1 = (self.book.gettype_of_book() * self.mul1)
        self.weight2 = (self.laptop.getWeight() * self.mul2)
        self.weight3 = (self.misc.getweight_m() * self.mul3)

        self.totaldis1var.set(str(self.weight1))
        self.totaldis2var.set(str(self.weight2))
        self.totaldis3var.set(str(self.weight3))

        #Calculate total weight and edit the Total weight label using StringVar
        self.bagWeight = self.weight1 + self.weight2 + self.weight3

        self.TOTlabel2var.set(str(self.bagWeight))

        #Bug proof the User weight input as well
        try: self.userWeight = int(self.we2var.get())
        except: pass
        self.limit = self.userWeight * 0.2

        #Create if statements for the bag weight total color and text
        if self.bagWeight < self.limit/2:
            self.boxcolor = "MediumSeaGreen"
            self.rectangle2var.set("Good bag weight!")
        elif self.bagWeight < self.limit:
            self.boxcolor = "Peru"
            self.rectangle2var.set("A little on the heavier side.")
        else:
            self.boxcolor = "IndianRed"
            self.rectangle2var.set("Too heavy!")
        
        self.myCanvas.itemconfigure(self.rectangle,fill = self.boxcolor) # change color of rectangle


program = program()

program.window.mainloop()

    
