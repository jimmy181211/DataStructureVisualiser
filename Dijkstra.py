from queueADT import Queue
import sys


class Vertex:
    def __init__(self,name):
        self.__name=name
        self.edges=[]
        self.visited=False #if the vertex has been visited
        self.prevVertex=None
        self.cost=sys.float_info[0]

    def getName(self):
        return self.__name


class Edge:
    def __init__(self,linked:Vertex,weight:int):
        self.linked=linked
        self.weight=weight


def search(v:Vertex,type:bool)->list:
    lst=[]
    if type:
        DFS(v,lst)
    else:
        BFS(v,lst)
    return lst


def DFS(v:Vertex, lst:list):
    v.visited=True
    edges=v.edges
    lst.append(v.getName())
    for edge in edges:
        if not edge.linked.visited:
            DFS(edge.linked,lst)


def BFS(v:Vertex,lst:list):
    queue=Queue(100)
    queue.add(v)
    while not queue.isEmpty():
        for edge in queue.get().edges:
            queue.add(edge.linked)
        lst.append(queue.remove().getName())


def dijkstra(v0:Vertex,vertices:list,target:str):
    # construct a vertex map
    v0.cost=0
    while len(vertices)!=0:
        curr=minCostVertex(lst)
        if curr.getName()==target:
            return curr.cost
        updateCost(curr,vertices)
        vertices.remove(curr)


def updateCost(curr:Vertex,vertices:list):
    for edge in curr.edges:
        n=edge.linked
        if vertices.__contains__(n):
            newCost=curr.cost+edge.weight
            if n.cost>newCost:
                n.cost=newCost


def minCostVertex(vertices:list):
    min_=vertices[0]
    for i in range(len(vertices)):
        if vertices[i].cost<min_.cost:
            min_=vertices[i]
    return min_


if __name__=="__main__":
    print("hello world")
    print(sys.float_info[0])
    lst=[1,2,3,4]
    print(lst.__contains__(9))