import sys
from itertools import permutations, combinations

v = int(sys.argv[1])
lo = [list(p) for p in permutations(range(1, (v + 1)))]

output = open(f"inputs/{v}vertices.txt", "w")
for i in range(len(lo)):
    lst = [list(p) for p in combinations(lo, (i + 1))]
    output.write(f"Number of linear orders: {i + 1}\n")
    for j in lst:
        output.write(('-'.join(str(k) for k in j))+'\n')
output.close()

print(f"Generated all linear order sets with {v} vertices")