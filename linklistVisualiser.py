from tkinter import *
from linkList import LinkList
from controlBlock import ControlBlock


class LinkListVisualiser:
    def __init__(self):
        self.llk = LinkList()
        self.cb = ControlBlock(title="linklistVisualiser", pos=(150, 400), size=(80, 40))
        self.idxEntryVal = None
        self.tagStr = "data"
        self.ptrLen=10
        self.linLen=50
        self.radius=8
        self.arrowY=self.cb.by + self.cb.bHeight / 2

    def isInt(self, num):
        return len(num) == 1 and 48 <= ord(num) <= 57

    def addItem(self):
        added = self.cb.entryVal.get()
        idx = self.idxEntryVal.get()
        # reset the entries
        self.idxEntryVal.set("")
        self.cb.entryVal.set("")
        if added != "" and self.isInt(idx):
            state = self.llk.add(added, int(idx))
            if state:
                self.cb.operation = f"{added} is added at idx {idx}"
        elif added != "" and idx == "":
            state = self.llk.addAtEnd(added)
            if state:
                self.cb.operation = f"{added} is added at the end"
        else:
            self.cb.operation = "push empty item!"
        self.updateDisplay()

    def removeItem(self):
        idx = self.idxEntryVal.get()
        self.idxEntryVal.set("")
        print(self.llk.size)
        # if the index is invalid
        if not self.isInt(idx):
            self.cb.operation = "invalid index"
        elif 0 > int(idx) or int(idx) >= self.llk.size:
            self.cb.operation = "index out of range"
        else:
            removed = self.llk.remove(int(idx))
            self.cb.operation = f"{removed} is removed at index{idx}"
        self.updateDisplay()

    def getItem(self):
        idx = self.idxEntryVal.get()
        self.idxEntryVal.set("")
        print("execute")
        if not self.isInt(idx):
            self.cb.operation = "invalid index"
        elif 0 > int(idx) or int(idx) >= self.llk.size:
            self.cb.operation = "index out of range"
        else:
            item = self.llk.get(int(idx))
            self.cb.operation = f"{item} is getted at index {idx}"
        self.updateDisplay()

    def updateDisplay(self):
        self.drawStore()
        self.drawAnnotated()
        self.showLastOperation()

    def drawStore(self):
        # initialising
        x, y = [self.cb.bx, self.cb.by]
        self.cb.canvas.delete(self.cb.tagStr)
        # rectangle for the pseudo-head
        self.cb.canvas.create_rectangle(x, y, x + self.cb.bWidth, y + self.cb.bHeight, width=1, fill="lightGray")

        for i in range(self.llk.size):
            self.cb.canvas.create_oval(x + self.cb.bWidth / 4 * 3 - self.radius, self.arrowY - self.radius,
                                       x + self.cb.bWidth / 4 * 3 + self.radius,
                                       self.arrowY + self.radius, width=1, fill="red", tag=self.cb.tagStr)
            x += self.cb.bWidth
            nextX = x + self.linLen + self.ptrLen
            # draw the rectangle
            self.cb.canvas.create_rectangle(nextX, y, nextX + self.cb.bWidth, y + self.cb.bHeight, width=1, fill="lightGray",tag=self.cb.tagStr)
            self.cb.canvas.create_line(nextX + self.cb.bWidth / 2, y, nextX + self.cb.bWidth / 2, y + self.cb.bHeight,width=3,fill="black", tag=self.cb.tagStr)
            # draw the pointer
            self.cb.canvas.create_line(x - self.cb.bWidth / 4 + self.radius, self.arrowY, nextX, self.arrowY, width=2, fill="black",
                                       tag=self.cb.tagStr)
            self.cb.canvas.create_line(x + self.linLen, self.arrowY - 10, nextX, self.arrowY, width=2, fill="black",
                                       tag=self.cb.tagStr)
            self.cb.canvas.create_line(x + self.linLen, self.arrowY + 10, nextX, self.arrowY, width=2, fill="black",
                                       tag=self.cb.tagStr)
            # draw indices
            self.cb.canvas.create_text(nextX + self.cb.bWidth / 4 * 3, self.arrowY - self.cb.bHeight, text=str(i),tag=self.cb.tagStr)
            x = nextX

    def drawAnnotated(self):
        intv=self.ptrLen+self.linLen+self.cb.bWidth
        x, y = [self.cb.bx+intv, self.cb.by]
        self.cb.canvas.delete(self.tagStr)
        datalst = self.llk.getData()
        for i in range(self.llk.size):
            self.cb.canvas.create_text(x+self.cb.bWidth/3,y+self.cb.bHeight/2,text=datalst[i],tag=self.tagStr)
            x+=intv

    def showLastOperation(self):
        self.cb.canvas.delete("oper")
        y = self.cb.by - 2* self.cb.bHeight
        self.cb.canvas.create_text(self.cb.bx + self.cb.bWidth / 2, y, tag="oper", text=self.cb.operation,
                                   font=('Arial', self.cb.fontSize))

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
        self.idxEntryVal = StringVar()
        valEntryLabel = Label(root, text="enter data", font=("Arial", 14, "normal"))
        idxEntryLabel = Label(root, text="enter index", font=("Arial", 14, "normal"))
        dataEntry = Entry(root, textvariable=self.cb.entryVal, font=('Arial', self.cb.fontSize, 'normal'))
        idxEntry = Entry(root, textvariable=self.idxEntryVal, font=("Arial", self.cb.fontSize, "normal"))

        # set the buttons where the user can add/ remove elements
        addbtn = Button(root, text="add", command=self.addItem)
        removebtn = Button(root, text="remove", command=self.removeItem)
        peekbtn = Button(root, text="get", command=self.getItem)

        # set the positions of the components
        valEntryLabel.place(x=10, y=10)
        idxEntryLabel.place(x=250, y=10)
        idxEntry.place(x=200, y=50)
        dataEntry.place(x=10, y=50)
        addbtn.place(x=10, y=80)
        removebtn.place(x=10, y=110)
        peekbtn.place(x=10, y=140)

        frame.pack()
        self.updateDisplay()
        root.mainloop()


if __name__ == "__main__":
    llkVis = LinkListVisualiser()
    llkVis.visualise()
    print("execute here")
