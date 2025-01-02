from tkinter import *
from controlBlock import ControlBlock
from strategyADT import StrategyADT


class Visualiser:
    def __init__(self, adt,title="visualiser", colors=("gray", "orange")):
        self.cb = ControlBlock(title,colors)
        self.ds = StrategyADT(adt)

    def showLastOperation(self):
        self.cb.canvas.delete("oper")
        y=self.cb.by-self.ds.capacity*self.cb.bHeight
        self.cb.canvas.create_text(self.cb.bx+self.cb.bWidth/2,y , tag="oper", text=self.cb.operation, font=('Arial', self.cb.fontSize))

    def addItem(self):
        data = self.cb.entryVal.get()
        self.cb.entryVal.set("")
        if data != "":
            self.ds.add(data)
            self.cb.operation = "push item:" + data
        else:
            print("the value is none!")
            self.cb.operation = "push empty item"
        self.updateDisplay()

    def removeItem(self):
        data = self.ds.remove()
        if data is None:
            self.cb.operation = "pop empty item!"
        else:
            self.cb.operation = "pop item:" + data
        self.updateDisplay()

    def getItem(self):
        data = self.ds.get()
        if data is None:
            self.cb.operation = "peek empty item!"
        else:
            self.cb.operation = "peeked item:" + data
        self.updateDisplay()

    def drawStore(self):
        x, y = [self.cb.bx, self.cb.by]
        for i in range(self.ds.capacity):
            if i < self.ds.size:
                color = self.cb.dataFill
            else:
                color = self.cb.freeFill
            self.cb.canvas.create_rectangle((x, y, x + self.cb.bWidth, y + self.cb.bHeight), width=1, fill=color)
            y -= self.cb.bHeight

    def updateDisplay(self):
        self.drawStore()
        self.annotateStore()
        self.showLastOperation()

    def drawPtr(self,x,y,ptrname,direction):
        if direction:
            # draw the pointer
            self.cb.canvas.create_line(x, y - 10, x + 10, y, width=2, fill="red", tag=self.cb.tagStr)
            self.cb.canvas.create_line(x, y + 10, x + 10, y, width=2, fill="red", tag=self.cb.tagStr)
            self.cb.canvas.create_text(x - 30, y - 5, text=ptrname, tag=self.cb.tagStr,
                                       font=("Arial", self.cb.fontSize))
        else:
            self.cb.canvas.create_line(x-50, y - 10, x-60, y, width=2, fill="red", tag=self.cb.tagStr)
            self.cb.canvas.create_line(x-50, y + 10, x-60, y, width=2, fill="red", tag=self.cb.tagStr)
            self.cb.canvas.create_text(x -20, y - 5, text=ptrname, tag=self.cb.tagStr,
                                       font=("Arial", self.cb.fontSize))

    def annotateStore(self):
        x, y = [self.cb.bx + self.cb.bWidth / 2.2, self.cb.by + self.cb.bHeight / 2.2]
        datalst = self.ds.getData()
        self.cb.canvas.delete(self.cb.tagStr)
        for i in range(self.ds.size):
            self.cb.canvas.create_text(x, y, tag=self.cb.tagStr, text=datalst[i], font=('Arial', self.cb.fontSize),
                                       anchor=NW)
            y -= self.cb.bHeight
        y += self.cb.bHeight

        #make indices
        y2=self.cb.by+self.cb.bHeight/2.2
        for i in range(self.ds.capacity):
            self.cb.canvas.create_text(x-70,y2,tag=self.cb.tagStr,text=str(i))
            y2-=self.cb.bHeight

    def visualise(self):
        # initial settings
        bgWidth, bgHeight = [1200, 700]
        root = Tk()
        root.title(self.cb.title)
        # set the menu bar
        fileMenu = Menu(Menu(root))
        fileMenu.add_command(label="exit", command=root.destroy)

        frame = Frame(root)
        self.cb.canvas = Canvas(frame, bd=1, width=bgWidth, height=bgHeight)
        self.cb.canvas.grid(row=0, column=0, sticky=N + S + E + W)

        # date entry, and initialising cb attributes
        self.cb.entryVal = StringVar()
        entryLabel = Label(root, text="enter data", font=("Arial", 14, "normal"))
        entryLabel.place(x=10, y=10)
        dataEntry = Entry(root, textvariable=self.cb.entryVal, font=('Arial', self.cb.fontSize, 'normal'))

        # set the buttons where the user can add/ remove elements
        addbtn = Button(root, text="push", command=self.addItem)
        removebtn = Button(root, text="pop", command=self.removeItem)
        peekbtn = Button(root, text="peek", command=self.getItem)

        # set the positions of the components
        dataEntry.place(x=10, y=50)
        addbtn.place(x=10, y=80)
        removebtn.place(x=10, y=110)
        peekbtn.place(x=10, y=140)

        frame.pack()
        self.updateDisplay()
        root.mainloop()
