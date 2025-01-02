from abc import abstractmethod, ABCMeta

class ADT(metaclass=ABCMeta):
    def __init__(self):
        self.size=0

    @abstractmethod
    def get(self, idx=0): pass

    @abstractmethod
    def add(self, val, idx=0): pass

    @abstractmethod
    def remove(self, idx=0): pass

    @abstractmethod
    def getData(self): pass

if __name__=="__main__":
   print()