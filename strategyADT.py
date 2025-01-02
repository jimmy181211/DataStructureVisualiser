class StrategyADT:
    def __init__(self, adtObj):
        self.adt=adtObj

    @property
    def size(self):
        return self.adt.size

    @property
    def capacity(self):
        try:
            return self.adt.capacity
        except:
            return None

    def add(self,val,idx=0):
        return self.adt.add(val,idx)

    def remove(self,idx=0):
        return self.adt.remove(idx)

    def get(self,idx=0):
        return self.adt.get(idx)

    def getData(self):
        return self.adt.getData()

