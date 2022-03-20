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

def reset(counters):
    for i in range(len(counters)):
      counters[i] = i  

def indicesProcess(counters, sizeFullSet):
    lastIndex = sizeFullSet-1
    cur = len(counters)-1
    if counters[cur] != lastIndex:
        counters[cur] += 1
    else:
        didreset = False
        while(counters[cur] == lastIndex):
            if cur == 0:
                counters.append(0)
                reset(counters)
                didreset = True
                break
            lastIndex -=1
            cur -= 1
        if not(didreset):
            counters[cur] += 1
            for i in range(len(counters)-cur-1):
                counters[cur+i+1] = counters[cur]+i+1
        
fileInput = open("4vertices3p2.txt", "r")
lines = fileInput.readlines()
fileInput.close()
f = open("optimal4v3test3.txt", "w")
kawnt = 1
numVertices = 4
for setInput in lines:
    if setInput[0] == "N":
        continue
    print(kawnt)
    kawnt += 1
    f.write("Optimal Solution for input: {0}".format(setInput))
    setinput = inputConverter(setInput)
    # powerset = powersetGEN(setinput)
    hasOnePosetCover = []

    listsub = setinput
    sizeFullSet = len(listsub)
    counters = [0]
    while True:
        if len(counters) > sizeFullSet:
            break

        subset = []
        for i in counters:
            subset.append(listsub[i])

        orderedpairsSet = []
        for i in subset:
            orderedpairs_per_LO = []
            for j in range(len(i)):
                for k in range(len(i)-(j+1)):
                    orderedpairs_per_LO.append((i[j] , i[j+k+1]))
            orderedpairsSet.append(set(orderedpairs_per_LO))
        # print(subset)
        # print(orderedpairsSet)
        edges = list(set.intersection(*orderedpairsSet))
        if edges == []:
            indicesProcess(counters, sizeFullSet)
            continue
        checkIfVerticesComplete = []
        for i in edges:
            checkIfVerticesComplete.append(i[0])
            checkIfVerticesComplete.append(i[1])
        checkIfVerticesComplete = list(set(checkIfVerticesComplete))
        if(len(checkIfVerticesComplete) != numVertices):
            indicesProcess(counters, sizeFullSet)
            continue
        # print(edges)
        graph = Graph(edges, numVertices, list(tuple(x) for x in subset))

        getAllTopologicalOrders(graph)
        set1 = set(tuple(x) for x in subset)
        set2 = set(tuple(x) for x in graph.listofLO)
        if(set1 == set2):
            hasOnePosetCover.append(graph)

        indicesProcess(counters, sizeFullSet)

    listsub = hasOnePosetCover
    sizeFullSet = len(listsub)
    solutions = []
    counters = [0]
    while True:
        if len(counters) > sizeFullSet:
            break

        subset = []
        for i in counters:
            subset.append(listsub[i])

        lst = []
        for j in subset:
            lst.extend(j.listofLO)
        set1 = set(tuple(x) for x in lst)
        set2 = set(tuple(x) for x in setinput)
        if(set1 == set2):
            solutions.append((subset,lst))
            break

        lastIndex = sizeFullSet-1
        cur = len(counters)-1
        if counters[cur] != lastIndex:
            counters[cur] += 1
        else:
            didreset = False
            while(counters[cur] == lastIndex):
                if cur == 0:
                    counters.append(0)
                    reset(counters)
                    didreset = True
                    break
                lastIndex -=1
                cur -= 1
            if not(didreset):
                counters[cur] += 1
                for i in range(len(counters)-cur-1):
                    counters[cur+i+1] = counters[cur]+i+1

    print(solutions, len(listsub))
    minimum = len(solutions[0][0])
    f.write("Length of optimal solution: {0}\n".format(minimum))
    
    print("-------")
    f.write("-----\n")
    for j in solutions[0][0]:
        print(j.edges)
        f.write(str(j.edges)+'\n')
    f.write('\n')

f.close()