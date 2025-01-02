from abc import ABC

from ADT import ADT


class Stack(ADT, ABC):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.stk = [""] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def add(self, val: str, idx=0):
        if self.isFull():
            return False
        self.stk[self.size] = val
        self.size += 1
        return True

    def get(self,idx=0):
        if self.isEmpty():
            return None
        return self.stk[self.size - 1]

    def remove(self,idx=0):
        if self.isEmpty():
            return None
        self.size -= 1
        return self.stk[self.size]

    def getData(self):
        return self.stk
