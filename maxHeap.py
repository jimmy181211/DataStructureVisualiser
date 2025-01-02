from abc import ABC

from ADT import ADT


class Pair:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val


class MaxHeap(ADT,ABC):
    def __init__(self,capacity=10):
        super().__init__()
        self.hp=[Pair()]*capacity
        self.capacity=capacity

    def compare(self,a,b):
        return a>b

    def add(self,val,key=0):
        if self.isFull():
            return False
        self.size+=1
        self.__up(key,val)
        return True

    def replace(self,val,key):
        self.hp[self.hp.index(val)]=Pair(key,val)

    def remove(self,idx=0):
        if self.isEmpty():
            return None
        self.size-=1
        self.__swap(0,self.size)
        removed=self.hp[self.size]
        self.__down(0)
        return removed.val

    def get(self,idx=0):
        if self.isEmpty():
            return None
        return self.hp[0].val

    def __swap(self,a,b):
        temp=self.hp[a]
        self.hp[a]=self.hp[b]
        self.hp[b]=temp

    def __down(self,parent):
        left=parent*2+1
        right=left+1
        max=parent
        if left<self.size and self.compare(self.hp[left].key,self.hp[max].key):
            max=left
        if right<self.size and self.compare(self.hp[right].key,self.hp[max].key):
            max=right
        if parent!=max:
            self.__swap(max,parent)
            self.__down(parent)

    def isEmpty(self):
        return self.size==0

    def isFull(self):
        return self.size==self.capacity

    def __up(self,key,val):
        child=self.size-1
        parent=int((child-1)/2)
        while child>0 and self.compare(key,self.hp[parent].key):
            self.hp[child]=self.hp[parent]
            child=parent
            parent=int((child-1)/2)
        self.hp[child]=Pair(key,val)

    def getData(self):
        lst=[]
        for i in range(self.size):
            lst.append(self.hp[i])
        return lst


if __name__=="__main__":
    lst=[1,7,4,10,9,986]
    vals=["data1","data2","data3","msg2","msg1","3mgs"]
    maxhp=MaxHeap(6)
    for i in range(len(lst)):
        maxhp.add(vals[i],lst[i])
    for i in range(maxhp.size):
        print(maxhp.remove())
    print("execute")