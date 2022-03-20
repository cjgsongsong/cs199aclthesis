from classes import Poset, LinearOrder, Timer
from algorithms import algorithm2

def preprocess(input):
    input = input.strip('\n').split('-')
    
    inputSet = []
    for lo_raw in input:
        lo = [int(num) for num in lo_raw.strip('[]').split(',')]
        inputSet.append(LinearOrder(lo))
    
    return inputSet

#fileOutput = open("3valgo2.txt", "w")
fileInput = open("3vertices.txt", "r")
inputs = fileInput.readlines()
fileInput.close()

count = 1
numVertices = 3
timer = Timer()
for input in inputs:
    if input[0] == "N":
        continue

    print(count)
    count += 1

    upsilon = preprocess(input)
    print([u.relations for u in upsilon]) #
    #print(f"Optimal Solution for input: {input}")
    #f.write(f"Optimal Solution for input: {input}")