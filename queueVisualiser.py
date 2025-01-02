from queueADT import Queue
from visualiser import Visualiser
from tkinter import *


class QueueVisualiser(Visualiser):
    def __init__(self, capacity=10):
        super().__init__(Queue(capacity))

    def annotateStore(self):
        datalst = self.ds.getData()
        yfront = self.cb.by + self.cb.bHeight / 2.2
        yend = yfront
        for i in range(self.ds.adt.bptr%self.ds.capacity):
            yend -= self.cb.bHeight
        x, y = [self.cb.bx + self.cb.bWidth / 2.2, yend]

        self.cb.canvas.delete(self.cb.tagStr)
        cnt = self.ds.adt.bptr
        while cnt != self.ds.adt.fptr:
            self.cb.canvas.create_text(x, y, tag=self.cb.tagStr, text=datalst[cnt%self.ds.adt.capacity],
                                       font=('Arial', self.cb.fontSize),
                                       anchor=NW)
            y -= self.cb.bHeight
            print("hello")
            cnt += 1
            if y<=self.cb.by+self.cb.bHeight/2.2-self.cb.bHeight*self.ds.capacity:
                y = self.cb.by + self.cb.bHeight / 2.2

        # make indices
        y2 = self.cb.by + self.cb.bHeight / 2.2
        for i in range(self.ds.capacity):
            self.cb.canvas.create_text(x - 70, y2, tag=self.cb.tagStr, text=str(i))
            y2 -= self.cb.bHeight

        for i in range(self.ds.adt.fptr%self.ds.capacity):
            yfront -= self.cb.bHeight
        self.drawPtr(self.cb.bx + self.cb.bWidth / 2.2 - 100, yfront, "frontptr", True)
        self.drawPtr(self.cb.bx + self.cb.bWidth + 80, yend, "endptr", False)

    def drawStore(self):
        x, y = [self.cb.bx, self.cb.by]
        fptr = self.ds.adt.fptr % self.ds.capacity
        bptr = self.ds.adt.bptr % self.ds.capacity
        for i in range(self.ds.capacity):
            if (fptr < bptr and (i < fptr or i >= bptr)) or (fptr > bptr and (bptr <= i < fptr)) or self.ds.adt.isFull():
                color = self.cb.dataFill
            else:
                color = self.cb.freeFill
            self.cb.canvas.create_rectangle((x, y, x + self.cb.bWidth, y + self.cb.bHeight), width=1, fill=color)
            y -= self.cb.bHeight


if __name__ == "__main__":
    queueVis = QueueVisualiser(5)
    queueVis.visualise()
