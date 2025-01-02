from stackADT import Stack

class TreeNode:
    def __init__(self,val=""):
        self.val=val
        self.left=None
        self.right=None


def compareTo(str1,str2):
    for i in range(min(len(str1),len(str2))):
        if ord(str1[i])>ord(str2[i]):
            return str1
        elif ord(str1[i])<ord(str2[i]):
            return str2
    if len(str1)==len(str2):
        return None
    elif len(str1)>len(str2):
        return str1
    else:
        return str2


def sort(lst):
    for i in range(len(lst)):
        base=lst[i]
        j=i-1
        while j>=0 and compareTo(lst[j],base)==lst[j]:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=base
    return lst


class BinarySearchTree:
    def __init__(self,dataList):
        self.root=TreeNode(sort(dataList)[int(len(dataList)/2)])
        for i in dataList:
            if i!=self.root:
                self.insertItem(self.root,i)
        self.size=len(dataList)

    @staticmethod
    def insertItem(node,val):
        if node is None:
            return TreeNode(val)
        if node.val>val:
            node.left=BinarySearchTree.insertItem(node.left,val)
        elif node.val<val:
            node.right=BinarySearchTree.insertItem(node.right,val)
        return node

    def findItem(self,node,val):
        if node is None:
            return None
        if node.val>val:
            self.findItem(node.left,val)
        elif node.val<val:
            self.findItem(node.right,val)
        else:
            return

    def getDataInner(self,node,lst):
        if node==None:
            return
        lst.append(node.val)
        self.getDataInner(node.left,lst)
        self.getDataInner(node.right,lst)

    def getData(self):
        lst=[]
        self.getDataInner(self.root,lst)
        return lst
#end class

def main():
    lst=["id","cb","ck","ay","a","k"]
    bstree=BinarySearchTree(lst)
    result=bstree.getData()
    for i in result:
        print(i)



if __name__=="__main__":
    main()