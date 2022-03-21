import fileinput
from classes import LinearOrder, Timer
from algorithms import algorithm2

def preprocess(input, toLO = True):
    input = input.strip('\n')
    
    if not toLO:
        return input
    else:
        inputSet = []
        for lo_raw in input.split('-'):
            lo = [int(num) for num in lo_raw.strip('[]').split(',')]
            inputSet.append(LinearOrder(lo))
        
        return inputSet

fileOutput = open("algo2/3valgo2.txt", "w")
fileInput = open("inputs/3vertices.txt", "r")
inputs = fileInput.readlines()
fileInput.close()

count = 1
numVertices = 3
timer = Timer()
for input in inputs:
    if input[0] == "N":
        fileOutput.write(f"Size ={input.split(':')[1]}\n")
        continue

    print(count)
    count += 1

    timer.start()
    solution = algorithm2(preprocess(input))
    #print(f"Time elapsed: {timer.stop():0.8f} seconds")
    #print(f"Approximation for input: {preprocess(input, False)}")
    #print(f"Approximation cost: {len(solution)}")
    fileOutput.write(f"Time elapsed: {timer.stop():0.8f} seconds\n")
    fileOutput.write(f"Approximation for input: {preprocess(input, False)}\n")
    fileOutput.write(f"Approximation cost: {len(solution)}\n")

    #print("-------")
    fileOutput.write("-----\n")
    for poset in solution:
        #print(poset.relations)
        fileOutput.write(f"{poset.relations}\n")
    #print('')
    fileOutput.write("\n")

fileOutput.close()

print("FINISH")