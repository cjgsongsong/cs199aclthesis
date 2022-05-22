import os, sys
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

def generateHammockRelations(parent, vertices, relations, isHammockLevel):
    # TO-DO: fix
    if len(vertices) == 1:
        return [sorted(relations)]
    else:
        rels = []
        for child in vertices:
            newVertices = [v for v in vertices if v != child]
            newRelations = relations + [(parent, child)]
            if isHammockLevel:
                rels.extend(generateHammockRelations(parent, newVertices, newRelations, True))
                rels.extend(generateHammockRelations(child, newVertices, newRelations, False))
            else:
                rels.extend(generateHammockRelations(child, newVertices, newRelations, True))
                rels.extend(generateHammockRelations(child, newVertices, newRelations, False))
        
        truerels = []
        for rel in rels:
            if rel not in truerels: truerels.append(rel)

        return rels

def generateRootedRelations(parent, vertices, relations):
    if len(vertices) == 0:
        return [sorted(relations)]
    else:
        rels = []
        for child in vertices:
            newVertices = [v for v in vertices if v != child]
            rels.extend(generateRootedRelations(parent, newVertices, relations + [(parent, child)]))
            rels.extend(generateRootedRelations(parent, newVertices, relations + [(child, parent)]))
            rels.extend(generateRootedRelations(child, newVertices, relations + [(parent, child)]))
            rels.extend(generateRootedRelations(child, newVertices, relations + [(child, parent)]))
        
        truerels = []
        for rel in rels:
            if rel not in truerels: truerels.append(rel)

        return truerels

if not os.path.exists("inputs/"):
    os.makedirs("inputs/")

args = sys.argv[1:]
args[1] = int(args[1])

if args[0] == 'all':
    lo = [list(p) for p in permutations(range(1, (args[1] + 1)))]
    output = open(f"inputs/{args[1]}vertices.txt", "w")
    for i in range(len(lo)):
        lst = [list(p) for p in combinations(lo, (i + 1))]
        output.write(f"Number of linear orders: {i + 1}\n")
        for j in lst:
            output.write(("-".join(str(k) for k in j))+"\n")
    output.close()

    print(f"Generated all linear order sets with {args[1]} vertices")
else:
    if not os.path.exists(f"inputs/{args[0]}/"):
        os.makedirs(f"inputs/{args[0]}/")

    vertices = [v for v in range(1, args[1] + 1)]
    rels = []
    for root in vertices:
        newVertices = [v for v in vertices if v != root]
        
        if args[0] == 'trees':
            rootedRels = generateRootedRelations(root, newVertices, [])
        elif args[0] == 'hammocks':
            rootedRels = generateHammockRelations(root, newVertices, [], False)
        
        for rel in rootedRels:
            if isAllConnected(vertices, rel) and rel not in rels: 
                rels.append(rel)

    lst = [Poset(args[1], relations).generateLinearExtensions() for
           relations in rels]
    output = open(f"inputs/{args[0]}/{args[1]}{args[0]}.txt", "w")
    for i in lst:
        output.write(("-".join(str(j) for j in i))+"\n")
    output.close()

    print(f"Generated all linear order sets of {args[0]} with {args[1]} vertices")