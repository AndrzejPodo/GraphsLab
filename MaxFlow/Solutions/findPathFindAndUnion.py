import sys
sys.path.append('/home/andrzej/GraphsLab/MaxFlow/GraphReader')
import dimacs

class Vertex:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.ownedSetSize = 1

def find(vertex):
    while vertex.parent != vertex:
        vertex = vertex.parent
    return vertex

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1.ownedSetSize > v2.ownedSetSize:
        v2.parent = v1
        v1.ownedSetSize += v2.ownedSetSize
    else:
        v1.parent = v2
        v2.ownedSetSize += v1.ownedSetSize

def findBestPath(G, s, t):
    V = []
    for i in range(1, G[0]+1):
        V.append(Vertex(i))
    L = G[1]
    L = sorted(L, key=lambda edge: edge[2], reverse = True)
    for edge in L:
        union(V[edge[0]-1], V[edge[1]-1])
        if find(V[s-1]) == find(V[t-1]):
            return edge[2]
    

print(findBestPath(dimacs.loadWeightedGraph(sys.argv[1]),1,2))



