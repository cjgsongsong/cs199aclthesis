import fileinput
from itertools import chain, combinations

def powersetGEN(setOflinearorders):
    lst = []
    for r in range(len(setOflinearorders)+1):
        lst.append([list(p) for p in combinations(setOflinearorders, r)])
    return list(chain.from_iterable(lst))

def inputConverter(input):
    perSet = []
    x = input.strip('\n').split('-')
    for j in x:
        converted = [int(num) for num in j.strip('[]').split(',')]
        perSet.append(converted)
    print(perSet)
    return perSet

def unionOfPosets(posets):
    lst = []
    for r in range(len(posets)+1):
        combination = [list(p) for p in combinations(posets, r)]
        lst.append(combination)
    return list(chain.from_iterable(lst))

def findAllTopologicalOrders(graph, path, marked, N):
    for v in range(N):
        if graph.indegree[v] == 0 and not marked[v]:
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] - 1
            path.append(v)
            marked[v] = True
            findAllTopologicalOrders(graph, path, marked, N)
 
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] + 1
 
            path.pop()
            marked[v] = False
 
    if len(path) == N:
        path = [i+1 for i in path]
        graph.listofLO.append(path.copy())
        print(path)

def getAllTopologicalOrders(graph):
    lenNodes = len(graph.adjList)
    marked = [False] * lenNodes
    path = []
    findAllTopologicalOrders(graph, path, marked, lenNodes)


class Graph:
    def __init__(self, edges, N, inputs):
        self.inputLO = inputs
        self.listofLO = [] 
        self.edges = edges
        #adjacency list
        self.adjList = [[] for _ in range(N)]

        # initialize in-degree of each vertex by 0
        self.indegree = [0] * N
        # add edges to the undirected graph
        for (src, dst) in edges:
            # add an edge from source to destination
            self.adjList[src-1].append(dst-1)
 
            # increment in-degree of destination vertex by 1
            self.indegree[dst-1] = self.indegree[dst-1] + 1
 

fileInput = open("4verticestest.txt", "r")
lines = fileInput.readlines()
fileInput.close()
f = open("optimal4vtest.txt", "w")
for setInput in lines:
    if setInput[0] == "N":
        continue
    f.write("Optimal Solution for input: {0}".format(setInput))
    setinput = inputConverter(setInput)
    powerset = powersetGEN(setinput)

    hasOnePosetCover = []

    for seT in powerset:
        if seT == []:
            continue
        orderedpairsSet = []
        for i in seT:
            orderedpairs_per_LO = []
            for j in range(len(i)):
                for k in range(len(i)-(j+1)):
                    orderedpairs_per_LO.append((i[j] , i[j+k+1]))
            orderedpairsSet.append(set(orderedpairs_per_LO))

        print(set.intersection(*orderedpairsSet))
        edges = list(set.intersection(*orderedpairsSet))
        graph = Graph(edges, 4, list(tuple(x) for x in seT))

        getAllTopologicalOrders(graph)
        set1 = set(tuple(x) for x in seT)
        set2 = set(tuple(x) for x in graph.listofLO)
        print(set1, set2)
        if(set1 == set2):
            hasOnePosetCover.append(graph)

    combi = unionOfPosets(hasOnePosetCover)
    solutions = []
    print(powerset)
    for i in combi:
        lst = []
        for j in i:
            lst.extend(j.listofLO)
        set1 = set(tuple(x) for x in lst)
        set2 = set(tuple(x) for x in setinput)
        if(set1 == set2):
            solutions.append((i,lst))

    numOfElements = [len(i) for i,l in solutions]
    minimum = min(numOfElements)
    indices = [i for i, v in enumerate(solutions) if len(v[0]) == minimum]
    print(len(indices))
    f.write("Length of optimal solution: {0}\n".format(minimum))
    f.write("Number of optimal solutions: {0}\n".format(len(indices)))
    for i in indices:
        print("-------")
        f.write("-----\n")
        for j in solutions[i][0]:
            print(j.edges)
            f.write(str(j.edges)+'\n')
        f.write('\n')
f.close()