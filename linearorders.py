import sys
from itertools import permutations, combinations
from classes import Poset

def isAllConnected(vertices, relations):
    for vertex in vertices:
        isConnected = False
        for relation in relations:
            if vertex in relation:
                isConnected = True
                break
        
        if not isConnected: return False
    
    return True

def generateRootedRelations(parent, vertices, relations):
    if len(vertices) == 0:
        return [relations]
    else:
        rels = []
        for child in vertices:
            newVertices = [v for v in vertices if v != child]
            newRelations = relations + [(parent, child)]
            rels.extend(generateRootedRelations(child, newVertices, relations))
            rels.extend(generateRootedRelations(child, newVertices, newRelations))
        
        return rels

args = sys.argv[1:]
args[1] = int(args[1])

if args[0] == 'tree':
    vertices = [v for v in range(1, args[1] + 1)]
    rels = []
    for root in vertices:
        newVertices = [v for v in vertices if v != root]
        rootedRels = generateRootedRelations(root, newVertices, [])
        for rel in rootedRels:
            if isAllConnected(vertices, rel) and rel not in rels: 
                rels.append(rel)

    lst = [Poset(args[1], relations).generateLinearExtensions() for
           relations in rels]
    output = open(f"inputs/trees/{args[1]}trees.txt", "w")
    for i in lst:
        output.write(("-".join(str(j) for j in i))+"\n")
    output.close()

    print(f"Generated all linear order sets of trees with {args[1]} vertices")

else:
    lo = [list(p) for p in permutations(range(1, (args[1] + 1)))]
    output = open(f"inputs/{args[1]}vertices.txt", "w")
    for i in range(len(lo)):
        lst = [list(p) for p in combinations(lo, (i + 1))]
        output.write(f"Number of linear orders: {i + 1}\n")
        for j in lst:
            output.write(("-".join(str(k) for k in j))+"\n")
    output.close()

    print(f"Generated all linear order sets with {args[1]} vertices")