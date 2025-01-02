from abc import ABC

from ADT import ADT


class Node:
    def __init__(self,val=None,nextNode=None):
        self.val=val
        self.next=nextNode


class LinkList(ADT, ABC):
    def __init__(self):
        super().__init__()
        self.pseudohead=Node()

    def __findPrev(self,idx):
        node=self.pseudohead
        for i in range(idx):
            node=node.next
        return node
    def idxInRange(self,idx):
        return 0<=idx<self.size

    def add(self,val,idx=0)->bool:
        if idx>self.size or idx<0:
            return False
        newNode=Node(val=val)
        prev=self.__findPrev(idx)
        newNode.next=prev.next
        prev.next=newNode
        self.size+=1
        return True

    def addAtEnd(self,val):
        return self.add(val,self.size)

    def remove(self,idx=0):
        if not self.idxInRange(idx):
            return None
        prev=self.__findPrev(idx)
        removed=prev.next.val
        prev.next=prev.next.next
        self.size-=1
        return removed

    def get(self,idx=0):
        if not self.idxInRange(idx):
            return None
        return self.__findPrev(idx).next.val

    def getData(self):
        lst=[]
        node=self.pseudohead.next
        for i in range(self.size):
            lst.append(node.val)
            node=node.next
        return lst


if __name__=="__main__":
    lst=[2,1,4,3,2,7]
    llk=LinkList()
    for i in lst:
        llk.addAtEnd(i)
    llk.remove(2)
    lst=llk.getData()
    for i in lst:
        print(i)
