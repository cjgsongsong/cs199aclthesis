import fileinput
from classes import Timer
from algorithms import algorithm2
from utils import preprocess

fileOutput = open("algo2/3valgo2.txt", "w")
fileInput = open("inputs/3vertices.txt", "r")
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
    solution = algorithm2(preprocess(input))
    fileOutput.write(f"Time elapsed: {timer.stop():0.8f} seconds\n")
    fileOutput.write(f"Approximation for input: {preprocess(input, False)}\n")
    fileOutput.write(f"Approximation cost: {len(solution)}\n")

    fileOutput.write("-----\n")
    for poset in solution:
        fileOutput.write(f"{poset.relations}\n")
    fileOutput.write("\n")

fileOutput.close()

print("FINISH")