import sys, fileinput
from classes import Timer
from algorithmsv2 import algorithm2v2
from utils import preprocess

args = sys.argv[1:]
if len(args) < 3:
    args.append("")

fileOutput = open(f"{args[0]}/{args[1]}v{args[2]}{args[0]}.txt", "w")
fileInput = open(f"inputs/{args[1]}vertices{args[2]}.txt", "r")
inputs = fileInput.readlines()
fileInput.close()

count = 1
timer = Timer()
for input in inputs:
    if input[0] == "N":
        fileOutput.write(f"Size ={input.split(':')[1]}\n")
        continue

    print(count)
    count += 1

    timer.start()
    if args[0] == "algo2v2":
        solution = algorithm2v2(preprocess(input))
    fileOutput.write(f"Time elapsed: {timer.stop():0.8f} seconds\n")
    fileOutput.write(f"Approximation for input: {preprocess(input, False)}\n")
    fileOutput.write(f"Approximation cost: {len(solution)}\n")

    fileOutput.write("-----\n")
    for poset in solution:
        fileOutput.write(f"{poset.relations}\n")
    fileOutput.write("\n")

fileOutput.close()

print("FINISH")