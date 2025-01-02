class Entry:
    def __init__(self, hashVal=0, key="", val=""):
        self.hashVal = hashVal
        self.key = key
        self.val = val
        self.next = None


class HashMap:
    def __init__(self,capacity=8):
        self.capacity = capacity
        self.table = [Entry()] * self.capacity
        self.size = 0
        self.loadFactor = 0.75
        self.threshold = self.capacity * self.loadFactor

    def get(self, hash, key):
        idx = self.hash(hash)
        if self.table[idx].key=="":
            return None
        p = self.table[idx]
        while not p is None and not p.key =="":
            if p.key == key:
                return p.val
            p = p.next
        return None

    def put(self, hashVal, key, value):
        idx = self.hash(hashVal)
        if self.table[idx].key == "" and self.table[idx].val == "":
            self.table[idx] = Entry(hashVal,key, value)
        else:
            p = self.table[idx]
            while True:
                if p.key == key:
                    p.val = value
                    return
                if p.next is None:
                    break
                p = p.next
            p.next = Entry(hashVal,key, value)
        self.size += 1
        #resize the hashMap
        if self.size > self.threshold:
            self.resize()

    def resize(self):
        self.capacity*=2
        newTable = [Entry()] * self.capacity
        for i in range(len(self.table)):
            p = self.table[i]
            ######
            a = None
            b = None
            aHead = None
            bHead = None
            while p is not None:
                if p.hashVal & len(self.table) == 0:
                    if not a is None:
                        a.next = p
                    else:
                        aHead = p
                    a = p
                else:
                    if not b is None:
                        b.next = p
                    else:
                        bHead = p
                    b = p
                p = p.next
            # change the tail pointer
            if a is not None:
                a.next = None
                newTable[i] = aHead
            if b is not None:
                b.next = None
                newTable[i + len(self.table)] = bHead
        self.table = newTable
        self.threshold=len(self.table)*self.loadFactor#renew the threshold as the size becomes bigger

    def hash(self, hashVal):
        return hashVal % len(self.table)

    def remove(self, hashVal, key):
        idx = self.hash(hashVal)
        if self.table[idx].key == "":
            return None
        p = self.table[idx]
        prev = None
        while p is not None:
            # if the target is found
            if p.key == key:
                # delete the first element
                if prev is None:
                    self.table[idx] = p.next
                # delete the other elements
                else:
                    prev.next = p.next
                self.size -= 1
                return p.val
            prev = p
            p = p.next
        return None

    def getData(self):
        result=[]
        for i in self.table:
            if i.key=="":
                continue
            p=i
            subList=[]
            while p is not None:
                subList.append(p)
                p=p.next
            result.append(subList)
        return result


if __name__ == "__main__":
    hashMap = HashMap()
    hashes=[3,10,32,48,21,81,98]
    keys=["maths","computer science","English","economics","history","physics","?"]
    values=["90%","82%","69%","65%","78%","84%","10%"]
    for i in range(len(keys)):
        hashMap.put(hashVal=hashes[i],key=keys[i],value=values[i])

    print(hashMap.get(3,"math"))
    lst=hashMap.getData()
    for i in lst:
        for j in i:
            print(j.hashVal,j.key,j.val)
        print()
