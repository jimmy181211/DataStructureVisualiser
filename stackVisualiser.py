from stackADT import Stack
from visualiser import Visualiser


class StackVisualiser(Visualiser):
    def __init__(self, capacity=10):
        super().__init__(Stack(capacity))

    def annotateStore(self):
        super().annotateStore()
        y=self.cb.by+self.cb.bHeight/2.2
        for i in range(self.ds.size):
            y-=self.cb.bHeight
        self.drawPtr(self.cb.bx+self.cb.bWidth/2.2-100,y,"currptr",True)

if __name__ == "__main__":
    stkVis = StackVisualiser()
    stkVis.visualise()
