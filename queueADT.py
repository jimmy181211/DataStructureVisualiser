from abc import ABC

from ADT import ADT


class Queue(ADT,ABC):
    def __init__(self, capacity):
        self.queue = [""] * capacity
        self.capacity=capacity
        super().__init__()
        self.fptr = 0
        self.bptr = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == len(self.queue)

    def add(self, val,idx=0):
        if self.isFull():
            return False
        self.queue[self.fptr%len(self.queue)] = val
        self.fptr+=1
        self.size += 1
        return True

    def remove(self,idx=0):
        if self.isEmpty():
            return None
        removed=self.queue[self.bptr%len(self.queue)]
        self.bptr+=1
        self.size-=1
        return removed

    def get(self,idx=0):
        if self.isEmpty():
            return None
        return self.queue[self.bptr]

    def getData(self):
        return self.queue