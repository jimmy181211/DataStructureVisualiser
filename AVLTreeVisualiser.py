from tkinter import *
from controlBlock import ControlBlock
from AVLTree import AVLTree, AVLNode
import math


class AVLTreeVisualiser:
    def __init__(self, capacity=8):
        self.cb = ControlBlock(title="visualiser", pos=(400, 100), size=(40, 40))
        self.avlTree = AVLTree(root=AVLNode(0, "defaultval"), maxSize=capacity)
        self.keyEntry = None
        self.capacity = capacity
        self.intv = capacity*self.cb.bWidth  # the number of node at the last layer*the size of one node
        self.r=self.cb.bWidth/2-2

    @staticmethod
    def isInt(num: str) -> bool:
        if num=="":
            return False
        if num[0]=="-":#negative number is accepted
            num=num[1:]
        for i in num:
            if not 48 <= ord(i) <= 57:
                return False
        return True

    def keySize(self,key:str):
        result=0
        size=10
        for char in key:
            result+=ord(char)*size
            size/=10
        return result

    def addItem(self):
        data = self.cb.entryVal.get()
        key = self.keyEntry.get()
        self.cb.entryVal.set("")
        self.keyEntry.set("")

        if data != "" and self.isInt(key):
            self.avlTree.put(int(key), data)
            self.cb.operation = f"add key-value pair: ({key},{data})"
        elif data!="" and key=="":
            self.avlTree.put(self.keySize(data),data)
            self.cb.operation=f"add value:{data}"
        elif not self.isInt(key):
            self.cb.operation = "invalid key!"
        elif data == "":
            self.cb.operation = "add empty item"
        self.updateDisplay()

    def updateDisplay(self):
        self.drawStore()
        self.showLastOperation()

    def removeItem(self):
        key = self.keyEntry.get()
        self.keyEntry.set("")
        if self.isInt(key):
            removed = self.avlTree.remove(int(key))
            self.cb.operation = f"{removed} at {key} is removed!"
        else:
            self.cb.operation = "invalid key!"
        self.updateDisplay()

    def getItem(self):
        key = self.keyEntry.get()
        self.keyEntry.set("")
        if self.isInt(key):
            get = self.avlTree.remove(int(key))
            self.cb.operation = f"{get} at {key} is removed!"
        else:
            self.cb.operation = "invalid key!"
        self.updateDisplay()

    def drawStore(self):
        self.cb.canvas.delete(self.cb.tagStr)
        x, y = [self.cb.bx, self.cb.by]
        intv = self.intv
        dataList = self.avlTree.getData()
        self.cb.canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r, width=2, fill="red",
                                   tag=self.cb.tagStr)
        self.cb.canvas.create_text(x, y, text=dataList[0][1], tag=self.cb.tagStr)
        root=AVLNode(*dataList[0])
        for i in range(1,len(dataList)):
            self.drawStoreIter(root,dataList[i],(x,y),intv)

    def drawStoreIter(self,node,pair,pos,intv,isLeft=True):
        if node is None:
            x,y=pos
            self.cb.canvas.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,width=2,fill="red",tag=self.cb.tagStr)
            self.cb.canvas.create_text(x,y,text=pair[1],tag=self.cb.tagStr)
            xLast=x+intv/2 if isLeft else x-intv/2
            self.cb.canvas.create_line(xLast,y-self.cb.bHeight+self.r,x,y-self.r,width=2,tag=self.cb.tagStr)
            return AVLNode(*pair)
        intv/=2 # at the beginning the intv is divided by two
        if pair[0]<node.key:
            node.left=self.drawStoreIter(node.left,pair,(pos[0]-intv/2,pos[1]+self.cb.bHeight),intv,True)
        elif pair[0]>node.key:
            node.right=self.drawStoreIter(node.right,pair,(pos[0]+intv/2,pos[1]+self.cb.bHeight),intv,False)
        return node

    def showLastOperation(self):
        self.cb.canvas.delete("operation")
        self.cb.canvas.create_text(self.cb.bx, self.cb.by - 50, font=('Arial', self.cb.fontSize, "normal"),
                                   text=self.cb.operation, tag="operation")

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
        valEntryLabel = Label(root, text="enter data", font=("Arial", 14, "normal"))
        keyEntryLabel = Label(root, text="enter key", font=("Arial", 14, "normal"))
        dataEntry = Entry(root, textvariable=self.cb.entryVal, font=('Arial', self.cb.fontSize, 'normal'))
        keyEntry = Entry(root, textvariable=self.keyEntry, font=("Arial", self.cb.fontSize, "normal"))
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
        self.updateDisplay()
        root.mainloop()


if __name__ == "__main__":
    avltreeVis = AVLTreeVisualiser()
    avltreeVis.visualise()
    print("execute")
