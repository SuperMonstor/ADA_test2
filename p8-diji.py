class Graph():
    def __init__(self, v, g):
        self.v = v
        self.graph = g

    def printans(self, parent, key):
        for x in range(1,self.v):
            print(str(parent[x]) + "->" +str(x) +"=" +str(key[x]))

    def findmax(self, key, mst):
        min = 999
        idx = -1
        for x in range(self.v):
            if(key[x] < min):
                min = key[x]
                idx = x
        return idx

    def findmin(self):
        key = [99] * self.v
        parent = [None] * self.v
        mst = [False] * self.v
        parent[0] = -1
        key[0] = 0

        for x in range(self.v):
            idx = self.findmax(key, mst)
            mst[idx] = True
            for y in range(self.v):
                if(key[y] > key[x] + graph[x][y] and graph[x][y] > 0 and mst[y] == False):
                    key[y] = key[x] + graph[x][y]
                    parent[y] = x
        self.printans(parent, key)

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
g = Graph(9, graph)

g.findmin();
