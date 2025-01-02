import sys


class AVLNode:
    def __init__(self, key=sys.float_info[0], val=""):
        self.val = val
        self.right = None
        self.left = None
        self.height = 1
        self.key = key


class AVLTree:
    def __init__(self, root=None, maxSize=100):
        self.root = root
        self.maxSize = maxSize
        self.__cnt = 0
        self.layer = 0
        self.size = 1
        self.isNext = False

    def compare(self,a,b):
        return a-b

    def isLeafNode(self, node):
        if node is None:
            return True
        return node.left is None and node.right is None

    def setHeights(self, node):
        if node is None:
            return 0
        node.height = max(self.setHeights(node.left), self.setHeights(node.right)) + 1
        return node.height

    def height(self, node):
        return 0 if node is None else node.height

    def updateHeight(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def __bf(self, node):
        return self.height(node.left) - self.height(node.right)

    def RRotate(self, node):
        top = node.left
        temp=top.right
        top.right=node
        node.left=temp
        self.updateHeight(node)
        self.updateHeight(top)
        return top

    def LRotate(self, node):
        top = node.right
        temp=top.left
        top.left=node
        node.right=temp
        self.updateHeight(node)
        self.updateHeight(top)
        return top

    def LRRotate(self, node):
        node.left = self.LRotate(node.left)
        return self.RRotate(node)

    def RLRotate(self, node):
        node.right = self.RRotate(node.right)
        return self.LRotate(node)

    def balance(self, node):
        if node is None:
            return None
        bf = self.__bf(node)
        temp = node
        if bf > 1 and self.__bf(node.left) >= 0:
            temp = self.RRotate(node)
        elif bf > 1 and self.__bf(node.left) < 0:
            temp = self.LRRotate(node)
        elif bf < -1 and self.__bf(node.right) > 0:
            temp = self.RLRotate(node)
        elif bf < -1 and self.__bf(node.right) <= 0:
            temp = self.LRotate(node)
        return temp

    def remove(self, key):
        if self.size > 0:
            self.size -= 1
            self.root = self.doRemove(self.root, key)

    def doRemove(self, node, key):
        if node is None:
            return None
        result=self.compare(key,node.key)
        if result<0:
            node.left = self.doRemove(node.left, key)
        elif not result>0:
            node.right = self.doRemove(node.right, key)
        else:  # the node is found
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.val = successor.val
                node.key = successor.key
                node.right = self.doRemove(node.right, successor.key)

        self.updateHeight(node)
        return self.balance(node)

    def put(self, key, val):
        if self.size < self.maxSize:
            self.size += 1
            self.root = self.doPut(self.root, key, val)

    def doPut(self, node, key, val):
        if node is None or node.key==sys.float_info[0]:
            return AVLNode(key, val)

        result=self.compare(key,node.key)
        if result==0:
            node.val = val
            return node
        if result<0:
            node.left = self.doPut(node.left, key, val)
        elif result>0:
            node.right = self.doPut(node.right, key, val)
        self.updateHeight(node)
        return self.balance(node)

    #preorder
    def getDataInner(self,node,lst):
        if node is None:
            return
        lst.append((node.key,node.val))
        self.getDataInner(node.left,lst)
        self.getDataInner(node.right,lst)

    def getData(self):
        lst=[]
        self.getDataInner(self.root,lst)
        return lst

    def traverse(self,x):
        lst=[]
        if x==1:
            self.postorder(self.root,lst)
        elif x==2:
            self.preorder(self.root,lst)
        return lst

    def postorder(self,node,lst):
        if node is None:
            return
        lst.append((node.key,node.val))
        self.getDataInner(node.left,lst)
        self.getDataInner(node.right,lst)

    def preorder(self,node,lst):
        if node is None:
            return
        self.getDataInner(node.left,lst)
        self.getDataInner(node.right,lst)
        lst.append((node.key, node.val))


if __name__ == "__main__":
    keys = [4, 2, 5, 30, 9, 7]
    vals = ["a", "d", "c", "e", "f", "j"]
    avlTree = AVLTree(AVLNode(0, "k"))
    for i in range(len(keys)):
        avlTree.put(keys[i], vals[i])

    dynarr = avlTree.traverse(1)
    for i in dynarr:
        print(i[0],i[1])

    dynarr2=avlTree.traverse(2)
    for i in dynarr2:
        print(i[0],i[1])


