
from collections import deque

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.visited = False

    def getVisited(self):
        return self.visited

    def setVisited(self, val):
        self.visited = val

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

 #   def __str__(self):
 #       return str(self.id) + ' connecte to : ' + str([x.id for x in self.connectedto])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        vertex = None
        if self.vertList.get(n, False):
            vertex = self.vertList[n]
        return vertex

    def __contains__(self, n):
        return n in self.vertList[n]

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def bfs_with_list(self, start):
        q = deque()
        q.append(start)
        exploredList = []

        while len(q) > 0:
            #import pdb; pdb.set_trace()
            currentVert = q[-1]
            notExplored = None
            print "exploring node ", currentVert.getId()
            for nbr in currentVert.getConnections():                
                if nbr.getId() not in exploredList and (nbr not in q):
                    notExplored = nbr
                    #break
            if notExplored is not None:
                q.append(notExplored)
            else:
                q.pop()
                exploredList.append(currentVert.getId())

    def bfs(self, start):
        q = deque()
        q.append(start)
        #exploredList = []

        while len(q) > 0:
            #import pdb; pdb.set_trace()
            currentVert = q[-1]
            notExplored = None
            print "exploring node ", currentVert.getId()
            for nbr in currentVert.getConnections():                
                if not nbr.getVisited() and (nbr not in q):
                    notExplored = nbr
                    #break
            if notExplored is not None:
                q.append(notExplored)
            else:
                q.pop()
                #exploredList.append(currentVert.getId())
                currentVert.setVisited(True)

    def dfs(self, start):
        #if start is None:
        #    return None

        #import pdb; pdb.set_trace()
        start.setVisited(True)
        print "Visted => ", start.getId()
        for nbr in start.getConnections():
            if not nbr.getVisited():                
                self.dfs(nbr)
        





""" 
Create a graph V = {V0, V1, V2, V3, V4, V5}
E = { (v0, v1, 5), (v1, v2, 4), (v2, v3, 9), (v3, v4, 7), (v4, v0, 1),
      (v0, v5, 2), (v5, v4, 8), (v3, v5, 3), (v5, v2, 1) }
"""

def createGraphV():
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    

    # add edge

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )") % (v.getId(), w.getId())

    #vert = g.getVertex

    #print g.bfs(vert)
    #print g.getVertices()
    print g.vertList.values()
    print g.vertList.keys()
    vert = g.vertList[0]
    #g.bfs(vert) # still work in progress
    print "***********************************"
    g.dfs(vert)

createGraphV()


#if __name__ == "__main__":
#    main()

