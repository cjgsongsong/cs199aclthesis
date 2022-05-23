import os, sys, fileinput
from classes import Graph, Timer
from itertools import chain, combinations
from utils import isAllConnected, generateRootedRelations

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

if not os.path.exists("optsol/"):
    os.makedirs("optsol/")

args = sys.argv[1:]
args[0] = int(args[0])

if len(args) > 1:
    input = open(f"inputs/{args[1]}/{args[0]}{args[1]}.txt", "r")
else:        
    input = open(f"inputs/{args[0]}vertices.txt", "r")
lines = input.readlines()
input.close()

count = 1
timer = Timer()
if len(args) > 1:
    if not os.path.exists(f"optsol/{args[1]}/"):
        os.makedirs(f"optsol/{args[1]}/")

    timer.start()
    vertices = [v for v in range(1, args[0] + 1)]
    lst = []
    for root in vertices:
        newVertices = [v for v in vertices if v != root]
        
        if args[1] == 'trees':
            rootedRels = generateRootedRelations(root, newVertices, [])
        
        for rel in rootedRels:
            if isAllConnected(vertices, rel) and rel not in lst: 
                lst.append(rel)
    time_elapsed = timer.stop()

    output = open(f"optsol/{args[1]}/{args[0]}voptsol.txt", "w")
    
    for i in range(len(lines)):
        output.write(f"Time elapsed: {(time_elapsed / len(lines)):0.8f} seconds\n")
        output.write(f"Input: {lines[i]}")
        output.write("Optimal solution cost: 1\n")
        output.write("-----\n")
        output.write(str(lst[i]) +"\n\n")
else:
    output = open(f"optsol/{args[0]}voptsol.txt", "w")

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
            graph = Graph(edges, args[0], list(tuple(x) for x in subset))
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