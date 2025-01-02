from tkinter import *
from maxHeap import MaxHeap
from controlBlock import ControlBlock
import math


class MaxHpVisualiser:
    def __init__(self, capacity=10):
        self.entryKey = None
        self.tagStr = "space"
        self.radius = 18
        self.intv = 180
        self.maxhp = MaxHeap(capacity)
        self.capacity=capacity
        self.cb = ControlBlock(title="heapVisualiser", pos=(300, 150), size=(42.86 * capacity, 40))

    def isInt(self, num: str) -> bool:
        for i in num:
            if not 48 <= ord(i) <= 57:
                return False
        return True

    def addItem(self):
        data = self.cb.entryVal.get()
        key = self.entryKey.get()
        self.cb.entryVal.set("")
        self.entryKey.set("")
        if self.maxhp.size==self.capacity:
            self.cb.operation="the maximum heap is full, unable to add items!"
        elif data != "" and self.isInt(key):
            self.maxhp.add(data, int(key))
            self.cb.operation = f"add key-value pair: ({key},{data})"
        elif not self.isInt(key):
            self.cb.operation = "invalid key!"
        elif data == "":
            self.cb.operation = "add empty item"
        self.updateDisplay()

    def removeItem(self):
        data = self.maxhp.remove()
        if data != "":
            self.cb.operation = f"delete value: {data}"
        else:
            self.cb.operation = "delete empty item"
        self.updateDisplay()

    def getItem(self):
        data = self.maxhp.get()
        if data != "":
            self.cb.operation = f"get value: {data}"
        else:
            self.cb.operation = "get empty item"
        self.updateDisplay()

    def drawSpace(self):
        x, y = [self.cb.bx, self.cb.by]
        for i in range(self.maxhp.capacity):
            self.cb.canvas.create_line(x, y, x + self.cb.bWidth, y, width=2, fill="black")
            # draw indices
            self.cb.canvas.create_text(x - 20, y + self.cb.bHeight / 2, text=str(i))
            y += self.cb.bHeight

    def drawStore(self):
        self.cb.canvas.delete(self.cb.tagStr)
        x, y = [self.cb.bx + self.cb.bWidth / 2 + self.intv / 2, self.cb.by + self.cb.bHeight / 2]
        xRow = x
        intv = self.intv
        dataList = self.maxhp.getData()
        coords = []
        for j in range(self.maxhp.size):
            if math.log(j + 1, 2) % 1 == 0:
                intv /= 2
                x -= intv
                xRow = x
            coords.append((xRow, y))
            xRow += 2 * intv
            y += self.cb.bHeight

        for i in range(self.maxhp.size):
            xRow, y = coords[i]
            # draw the circle
            self.cb.canvas.create_oval(xRow - self.radius, y - self.radius, xRow + self.radius, y + self.radius,
                                       width=2, fill="red", tag=self.cb.tagStr)
            # draw the rectangle for keys
            self.cb.canvas.create_rectangle(self.cb.bx + self.cb.bWidth, y - self.cb.bHeight / 2,
                                            self.cb.bx + self.cb.bWidth + self.cb.bHeight, y + self.cb.bHeight / 2,
                                            width=2, tag=self.cb.tagStr)
            # write keys
            self.cb.canvas.create_text(self.cb.bx + self.cb.bWidth + self.cb.bHeight / 2, y, text=dataList[i].key,
                                       tag=self.cb.tagStr)
            # write values
            self.cb.canvas.create_text(xRow, y, text=dataList[i].val, tag=self.cb.tagStr)
            if i*2+1<self.maxhp.size:
                #draw line: left child
                self.cb.canvas.create_line(xRow,y+self.radius,coords[i*2+1][0],coords[i*2+1][1]-self.radius,width=3,tag=self.cb.tagStr)
            if i*2+2<self.maxhp.size:
                #draw line: right child
                self.cb.canvas.create_line(xRow,y+self.radius,coords[i*2+2][0],coords[i*2+2][1]-self.radius,width=3,tag=self.cb.tagStr)


    def updateDisplay(self):
        self.drawStore()
        self.showLastOperation()

    def showLastOperation(self):
        self.cb.canvas.delete("operation")
        self.cb.canvas.create_text(self.cb.bx + self.cb.bWidth / 2, self.cb.by - 50, text=self.cb.operation,
                                   font=('Arial', self.cb.fontSize), tag="operation")

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
        self.entryKey = StringVar()
        valEntryLabel = Label(root, text="enter data", font=("Arial", 14, "normal"))
        keyEntryLabel = Label(root, text="enter key", font=("Arial", 14, "normal"))
        dataEntry = Entry(root, textvariable=self.cb.entryVal, font=('Arial', self.cb.fontSize, 'normal'))
        keyEntry = Entry(root, textvariable=self.entryKey, font=("Arial", self.cb.fontSize, "normal"))
        keyLabel = Label(root, text="key", font=("Arial", 14))
        # set the buttons where the user can add/ remove elements
        addbtn = Button(root, text="add", command=self.addItem)
        removebtn = Button(root, text="remove", command=self.removeItem)
        peekbtn = Button(root, text="get", command=self.getItem)

        # set the positions of the components
        keyLabel.place(x=self.cb.bx + self.cb.bWidth + self.cb.bHeight / 6, y=self.cb.by - 50)
        valEntryLabel.place(x=10, y=10)
        keyEntryLabel.place(x=250, y=10)
        keyEntry.place(x=200, y=50)
        dataEntry.place(x=10, y=50)
        addbtn.place(x=10, y=80)
        removebtn.place(x=10, y=110)
        peekbtn.place(x=10, y=140)

        frame.pack()
        self.drawSpace()
        self.updateDisplay()
        root.mainloop()


if __name__ == "__main__":
    maxhpVis = MaxHpVisualiser()
    maxhpVis.visualise()
    print("execute main")
