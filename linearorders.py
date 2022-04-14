from itertools import permutations, combinations
import sys

arg = int(sys.argv[1]) + 1
for v in range(3, arg):
    linearorders = [list(p) for p in permutations(range(1, (v + 1)))]

    fileOutput = open(f"inputs/{v}vertices.txt", "w")
    for i in range(len(linearorders)):
        lst = [list(p) for p in combinations(linearorders, (i + 1))]
        fileOutput.write(f"Number of linear orders: {i + 1}\n")
        for j in lst:
            fileOutput.write(('-'.join(str(k) for k in j))+'\n')
    fileOutput.close()

    print(f"Generated all linear order sets with {v} vertices")