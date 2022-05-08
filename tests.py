import sys
from classes import Timer
from algorithms import algorithm1, algorithm2
from utils import read, preprocess

args = sys.argv[1:]
if len(args) == 2:
    inputs = read(f"inputs/{args[1]}vertices.txt")
    output = open(f"{args[0]}/{args[1]}v{args[0]}.txt", "w")
else:
    inputs = read(f"inputs/{args[2]}/{args[1]}{args[2]}.txt")
    output = open(f"{args[0]}/{args[2]}/{args[1]}v{args[0]}.txt", "w")


count = 1
timer = Timer()
for input in inputs:
    if input[0] == "N":
        output.write(f"Size ={input.split(':')[1]}\n")
        continue

    print(count)
    count += 1

    timer.start()
    if args[0] == "algo1":
        solution = algorithm1(preprocess(input))
    elif args[0] == "algo2":
        solution = algorithm2(preprocess(input))
    output.write(f"Time elapsed: {timer.stop():0.8f} seconds\n")
    output.write(f"Input: {preprocess(input, False)}\n")
    output.write(f"Approximation cost: {len(solution)}\n")

    output.write("-----\n")
    for poset in solution:
        output.write(f"{poset.relations}\n")
    output.write("\n")

output.close()

print("FINISH")