import sys
from itertools import permutations, combinations
from classes import Poset

def generateTrees(size, parent, vertices, relations):
    if len(vertices) == 0:
        return [Poset(size, relations).generateLinearExtensions()]
    else:
        lst = []
        for child in vertices:
            newVertices = [v for v in vertices if v != child]
            newRelations = relations + [(parent, child)]
            lst.extend(generateTrees(size, child, newVertices, newRelations))
        
        return lst

args = sys.argv[1:]
args[1] = int(args[1])
if args[0] == 'tree':
    lst = []
    vertices = [v for v in range(1, args[1] + 1)]
    for root in vertices:
        newVertices = [v for v in vertices if v != root]
        lst.extend(generateTrees(max(vertices), root, newVertices, []))

    print(lst)
    #output = open(f"inputs/{args[1]}trees.txt", "w")
    #for i in lst:
    #    output.write(("-".join(str(j) for j in i))+"\n")
    #output.close()

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