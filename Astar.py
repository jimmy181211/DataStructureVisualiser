import sys


# I think the code is much more graceful than ISC's

class GraphNode:
    def __init__(self, name: str, heuristicVal=sys.maxsize):
        self.val = name
        self.heuristicVal = heuristicVal
        self.visited = False


# non-directed graph
# the adjacency matrix looks like this:
# {node1:{node2:cost,node4:cost},node2:{node3:cost}...}
class Graph:
    def __init__(self, nodeList: list):
        self.mtrx = {}
        # initialise the adjacency matrix, which is a dictionary
        for node in nodeList:
            self.mtrx[node] = {}

    def addLink(self, sourceNodeName: str, linkedNode: GraphNode, cost: float):
        for node in self.mtrx:
            if node.val == sourceNodeName:
                # link from the source to the target node
                self.mtrx[node][linkedNode] = cost
                # link from the target node to the source
                self.mtrx[linkedNode][node] = cost

    # returns all the nodes linked to the targetNode
    def linkedToNode(self, targetNode: GraphNode) -> list:
        lst = []
        for node in self.mtrx:
            if node == targetNode:
                # convert the dictionary to list
                for linked in self.mtrx[node]:
                    lst.append(linked)
        return lst

    def searchNode(self, name) -> GraphNode:
        for node in self.mtrx:
            if node.val == name:
                return node
        return GraphNode("", -1)

    def nodeAddLink(self, sourceNode: GraphNode, linkedNode: GraphNode, cost: float):
        for node in self.mtrx:
            if node == sourceNode:
                self.mtrx[node][linkedNode] = cost
                self.mtrx[linkedNode][node] = cost

    def addLinkByName(self, source: str, linked: str, cost: float):
        for node in self.mtrx:
            if node.val == source:
                linkedNode = self.searchNode(linked)
                self.mtrx[node][linkedNode] = cost
                self.mtrx[linkedNode][node] = cost

    def remove(self, sourceNodeName: str):
        for node in self.mtrx:
            if node.val == sourceNodeName:
                self.mtrx.pop(node)

    def getLinked(self, node) -> dict:
        return self.mtrx[node]


class Info:
    def __init__(self, cost=sys.maxsize, score=sys.maxsize, prevNode=None):
        self.cost = cost
        self.score = score
        self.prevNode = prevNode


class AStar:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.unvisited = {}
        self.__heuristicMap = {}

    def __get_min(self):
        # select a random node
        minNode = list(self.graph.mtrx.keys())[0]
        for node in self.unvisited:
            try:
                # if self.unvisited[node].score < self.unvisited[minNode].score:
                #     minNode = node
                self.unvisited[node].score
            except Exception:
                print(node.val)
                sys.exit(0)
        return minNode

    def getHeuristic(self, node: GraphNode):
        return self.__heuristicMap[node]

    def updateHeuristicMap(self, node: GraphNode, heuristicVal):
        for temp in self.graph.mtrx:
            if temp == node:
                # make sure this dictionary doesn't add graphNode that doesn't exit in mtrx
                self.__heuristicMap[temp] = heuristicVal

    def a_star(self, startName: str, targetName: str):
        start_node = self.graph.searchNode(startName)
        target_node = self.graph.searchNode(targetName)
        if start_node.val == "" and start_node.heuristicVal == -1 or target_node.val == "" and target_node.heuristicVal == -1:
            print("entered nodes are not found!")
            return None
        for node in self.graph.mtrx:
            # if the heuristic value is not initialised:
            if node.heuristicVal == sys.maxsize:
                node.heuristicVal = self.getHeuristic(node)
            self.unvisited[node] = Info()  # Info contians f-score, actual cost, and prevNode
        self.unvisited[start_node] = Info(0, 0, None)

        while len(self.unvisited) != 0:
            curr = self.__get_min()
            if curr == target_node:
                # return the cost and the prevNode to the client
                return [self.unvisited[curr].cost, self.unvisited[curr].prevNode]
            self.__update_score(curr)
            self.unvisited.pop(curr)
        # when it is not found
        return [-1, None]

    def __update_score(self, curr: GraphNode):
        linked = self.graph.getLinked(curr)
        for node in linked:
            # heuristicValue + the cost
            cost = linked[node] + self.unvisited[curr].cost
            score = cost + node.heuristicVal
            if self.unvisited[node].score > score:
                self.unvisited[node] = Info(cost, score, curr)


# don't overestimate the heuristics
if __name__ == "__main__":
    names = ["A", "B", "C", "D", "E", "F", "G", "H"]
    heuristics = [70, 53, 43, 30, 30, 15, 10, 0]
    nodes = []
    for i in range(len(names)):
        nodes.append(GraphNode(names[i], heuristics[i]))
    graph = Graph(nodes)
    links = [["A", "C", 24], ["A", "B", 16], ["B", "E", 23], ["C", "E", 11], ["C", "D", 18], ["E", "F", 13],
             ["D", "F", 15], ["D", "G", 23], ["F", "H", 20], ["G", "H", 15]]
    algorithm = AStar(graph)
    algorithm.a_star("A", "H")
