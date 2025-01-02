from tkinter import *
from BinarySearchTree import *
from controlBlock import ControlBlock


class BSTreeVisualiser:
    def __init__(self, dataList):
        self.cb = ControlBlock("binarySearchTree visualser", pos=(300, 100), size=(40, 40))
        self.bstree = BinarySearchTree(dataList)
        self.r = self.cb.bWidth / 2 - 2
        self.intv = self.bstree.size * self.cb.bHeight

    def doDrawStore(self, node, val, pos, intv, isLeft=True):
        if node is None:
            x, y = pos
            self.cb.canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r, fill="red")
            self.cb.canvas.create_text(x, y, text=val)
            xLast = x + intv / 2 if isLeft else x - intv / 2
            self.cb.canvas.create_line(xLast, y - self.cb.bHeight + self.r, x, y - self.r, width=2)
            return TreeNode(val)
        intv /= 2
        if compareTo(node.val, val) == node.val:
            node.left = self.doDrawStore(node.left, val, (pos[0] - intv / 2, pos[1] + self.cb.bHeight), intv, True)
        elif compareTo(node.val, val) == val:
            node.right = self.doDrawStore(node.right, val, (pos[0] + intv / 2, pos[1] + self.cb.bHeight), intv, False)
        return node

    def visualise(self):
        root = Tk()
        root.title(self.cb.title)
        filemenu = Menu(Menu(root))
        filemenu.add_command(label="exit", command=root.destroy)

        bgWidth, bgHeight = [1200, 700]
        frame = Frame(root)
        self.cb.canvas = Canvas(frame, bd=1, width=bgWidth, height=bgHeight)
        self.cb.canvas.grid(row=0, column=0, sticky=N + S + E + W)
        frame.pack()

        x, y = (self.cb.bx, self.cb.by)
        dataList = self.bstree.getData()
        root = TreeNode(dataList[0])
        self.cb.canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r, fill="red")
        self.cb.canvas.create_text(x, y, text=dataList[0])
        for i in range(1, len(dataList)):
            self.doDrawStore(root, dataList[i], (x, y), self.intv)

        self.cb.canvas.mainloop()


# end class

def main():#control function for the program
    datalist = ["id", "cb", "ck", "ay", "a", "k"]
    bstreeVis = BSTreeVisualiser(datalist)
    bstreeVis.visualise()
    print("execute")


if __name__ == "__main__":
    main()
