import sys, fileinput
from classes import Graph, Timer
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

v = int(sys.argv[1])        
input = open(f"inputs/{v}vertices.txt", "r")
lines = input.readlines()
input.close()

count = 1
timer = Timer()
output = open(f"optsol/{v}voptsol.txt", "w")
for setInput in lines:
    if setInput[0] == "N":
        output.write(f"Size = {setInput.split(':')[1][1:]}\n")
        continue
    
    print(count)
    count += 1
    
    timer.start()
    setinput = inputConverter(setInput)
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
        
        edges = list(set.intersection(*orderedpairsSet))
        if edges == []:
            indicesProcess(counters, sizeFullSet)
            continue
        checkIfVerticesComplete = []
        for i in edges:
            checkIfVerticesComplete.append(i[0])
            checkIfVerticesComplete.append(i[1])
        checkIfVerticesComplete = list(set(checkIfVerticesComplete))
        if(len(checkIfVerticesComplete) != v):
            indicesProcess(counters, sizeFullSet)
            continue
        
        graph = Graph(edges, v, list(tuple(x) for x in subset))

        graph.getAllTopologicalOrders()
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

    output.write(f"Time elapsed: {timer.stop():0.8f} seconds\n")
    output.write(f"Input: {setInput}")
    output.write(f"Optimal solution cost: {len(solutions[0][0])}\n")
    output.write("-----\n")
    for j in solutions[0][0]:
        output.write(str(j.edges)+"\n")
    output.write("\n")

output.close()

print("FINISH")