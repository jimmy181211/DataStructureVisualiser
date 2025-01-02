from tkinter import *
from controlBlock import ControlBlock
from hashMap import HashMap


class HashMapVisualiser:
    def __init__(self):
        self.cb = ControlBlock(title="hashmapVisualiser", pos=(500, 100), size=(150, 40))
        self.capacity = 16
        self.hashmap = HashMap(self.capacity)
        self.hashEntry = None
        self.keyEntry = None
        self.ptrLen = 10
        self.linLen = 50
        self.radius = 8
        self.arrowY = self.cb.by + self.cb.bHeight / 2

    @staticmethod
    def isInt(num: str) -> bool:
        if num == "":
            return False
        for i in num:
            if not 48 <= ord(i) <= 57:
                return False
        return True

    def addItem(self):
        hash = self.hashEntry.get()
        key = self.keyEntry.get()
        value = self.cb.entryVal.get()
        self.hashEntry.set("")
        self.keyEntry.set("")
        self.cb.entryVal.set("")

        if value != "" and key != "" and self.isInt(hash):
            self.cb.operation = f"enter {key}:{value}"
            self.hashmap.put(int(hash), key, value)
        elif not self.isInt(hash):
            self.cb.operation = f"invalid hashcode!"
        else:
            self.cb.operation = "unable to add the item!"
        self.updateDisplay()

    def removeItem(self):
        hash = self.hashEntry.get()
        key = self.keyEntry.get()
        self.hashEntry.set("")
        self.keyEntry.set("")

        if key!="" and self.isInt(hash):
            val=self.hashmap.remove(hash,key)
            if val is None:
                self.cb.operation=f"hashcode or key is not found!"
            else:
                self.cb.operation=f"{key}:{val} is removed!"
        elif not self.isInt(hash):
            self.cb.operation="the hashcode is not valid!"
        else:
            self.cb.operation="unable to remove the item!"
        self.updateDisplay()

    def getItem(self):
        hash = self.hashEntry.get()
        key = self.keyEntry.get()
        self.hashEntry.set("")
        self.keyEntry.set("")

        if key != "" and self.isInt(hash):
            value = self.hashmap.remove(hash, key)
            if value is None:
                self.cb.operation = "key or hashValue not found!"
            else:
                self.cb.operation = f"{key}:{value} is removed"
        elif not self.isInt(hash):
            self.cb.operation = "invalid hashcode!"
        else:
            self.cb.operation = "can't remove the item!"
        self.updateDisplay()

    def updateDisplay(self):
        self.drawStore()
        self.showLastOperation()

    def drawStore(self):
        self.cb.canvas.delete(self.cb.tagStr)
        list2D = self.hashmap.getData()
        x, y = [self.cb.bx, self.cb.by]
        arrowY=self.arrowY

        for dataList in list2D:
            self.cb.canvas.create_rectangle(x, y, x + self.cb.bWidth, y + self.cb.bHeight, width=2, tag=self.cb.tagStr,fill="lightGray")
            self.cb.canvas.create_text(x +self.cb.bWidth/4, y+self.cb.bHeight/2, tag=self.cb.tagStr, text=f"{dataList[0].key}:{dataList[0].val}")
            self.cb.canvas.create_line(x + self.cb.bWidth / 2, y, x + self.cb.bWidth / 2,
                                       y + self.cb.bHeight, width=3, fill="black", tag=self.cb.tagStr)
            innerX=x
            for i in range(1, len(dataList)):
                self.cb.canvas.create_oval(innerX + self.cb.bWidth / 4 * 3 - self.radius, arrowY - self.radius,
                                           innerX + self.cb.bWidth / 4 * 3 + self.radius,
                                           arrowY + self.radius, width=1, fill="red", tag=self.cb.tagStr)
                innerX += self.cb.bWidth
                nextX = innerX + self.linLen + self.ptrLen
                # draw the rectangle
                self.cb.canvas.create_rectangle(nextX, y, nextX + self.cb.bWidth, y + self.cb.bHeight, width=2,
                                                fill="lightGray", tag=self.cb.tagStr)
                self.cb.canvas.create_line(nextX + self.cb.bWidth / 2, y, nextX + self.cb.bWidth / 2,
                                           y + self.cb.bHeight, width=3, fill="black", tag=self.cb.tagStr)
                #draw text
                self.cb.canvas.create_text(nextX+self.cb.bWidth/4, y +self.cb.bHeight/2, text=f"{dataList[i].key}:{dataList[i].val}+",
                                           tag=self.cb.tagStr)
                # draw the pointer
                self.cb.canvas.create_line(innerX - self.cb.bWidth / 4 + self.radius, arrowY, nextX, arrowY,
                                           width=2, fill="black",
                                           tag=self.cb.tagStr)
                self.cb.canvas.create_line(innerX + self.linLen, arrowY - 10, nextX, arrowY, width=2, fill="black",
                                           tag=self.cb.tagStr)
                self.cb.canvas.create_line(innerX + self.linLen, arrowY + 10, nextX, arrowY, width=2, fill="black",
                                           tag=self.cb.tagStr)
                innerX = nextX
            y += self.cb.bHeight
            arrowY+=self.cb.bHeight


    def showLastOperation(self):
        self.cb.canvas.delete("operation")
        x,y=[self.cb.bx,self.cb.by-50]
        self.cb.canvas.create_text(x,y,text=self.cb.operation,font=("Arial",self.cb.fontSize,"normal"),tag="operation")

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
        self.keyEntry = StringVar()
        self.hashEntry = StringVar()
        valEntryLabel = Label(root, text="enter data", font=("Arial", 14, "normal"))
        keyEntryLabel = Label(root, text="enter key", font=("Arial", 14, "normal"))
        hashEntryLabel = Label(root, text="enter hashCode", font=("Arial", 14, "normal"))
        hashEntry = Entry(root, textvariable=self.hashEntry, font=('Arial', self.cb.fontSize, 'normal'))
        dataEntry = Entry(root, textvariable=self.cb.entryVal, font=('Arial', self.cb.fontSize, 'normal'))
        keyEntry = Entry(root, textvariable=self.keyEntry, font=("Arial", self.cb.fontSize, "normal"))

        # set the buttons where the user can add/ remove elements
        addbtn = Button(root, text="add", command=self.addItem)
        removebtn = Button(root, text="remove", command=self.removeItem)
        peekbtn = Button(root, text="get", command=self.getItem)

        # set the positions of the components
        valEntryLabel.place(x=10, y=10)
        keyEntryLabel.place(x=250, y=10)
        hashEntryLabel.place(x=10,y=80)
        hashEntry.place(x=10,y=120)
        keyEntry.place(x=200, y=50)
        dataEntry.place(x=10, y=50)
        addbtn.place(x=10, y=150)
        removebtn.place(x=10, y=180)
        peekbtn.place(x=10, y=210)

        frame.pack()
        self.updateDisplay()
        root.mainloop()
#end class

def main():
    hashMapVis=HashMapVisualiser()
    hashMapVis.visualise()
    print("execute")

if __name__ == "__main__":
    main()
