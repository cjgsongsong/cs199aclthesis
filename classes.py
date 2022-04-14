import time

INVALID = -1
Sequence = list[int]
Vertices = list[int]
Relations = list[tuple[(int, int)]]
LinearOrders = list[list[int]]

class Poset():

    def __init__(self, relations: Relations):
        # Vertex V with no relations is inputted as (V, -1)
        self.relations = self._preprocessRelations(relations)
        self.vertices = self._getVertices(self.relations)
    
    def _getVertices(self, relations: Relations) -> Vertices:
        vertices = []
        for relation in relations:
            if relation[0] not in vertices:
                vertices.append(relation[0])

            if relation[1] not in vertices:
                vertices.append(relation[1]) 
        
        return sorted(vertices)

    def _preprocessRelations(self, relations: Relations) -> Relations:
        for relation in relations:
            if relation[1] == INVALID:
                relations.pop(relation)
        
        return sorted(relations)

    def subtract(self, poset: "Poset") -> Relations:
        relations = []
        for relation in self.relations:
            if relation not in poset.relations:
                relations.append(relation)

        return relations

    #def transitiveReduce(self) -> None:
        #pass

    #def generateLinearExtensions(self) -> LinearOrders:
        #pass

class LinearOrder(Poset):

    def __init__(self, sequence: Sequence):
        self.sequence = sequence
        super().__init__(self._getRelations(sequence))

    def _getRelations(self, sequence: Sequence) -> Relations:
        relations = []
        for i in range(0, len(sequence) - 1):
            for j in range(i + 1, len(sequence)):
                relations.append((sequence[i], sequence[j]))
        
        return relations

class Graph:
    def __init__(self, edges, N, inputs):
        self.inputLO = inputs
        self.listofLO = [] 
        self.edges = edges
        self.adjList = [[] for _ in range(N)]

        # initialize in-degree of each vertex by 0
        self.indegree = [0] * N
        # add edges to the undirected graph
        for (src, dst) in edges:
            # add an edge from source to destination
            self.adjList[src-1].append(dst-1)
 
            # increment in-degree of destination vertex by 1
            self.indegree[dst-1] = self.indegree[dst-1] + 1

class Timer:

    def __init__(self):
        self._start_time = None
    
    def start(self):
        self._start_time = time.perf_counter()
    
    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        return elapsed_time