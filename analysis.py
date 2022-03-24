import fileinput
from utils import preprocess, split, extract

fileInput = open("algo2/3valgo2.txt", "r")
inputs = fileInput.readlines()
fileInput.close()

algo2 = []
for input in split(inputs):
    if len(input) != 1:
        algo2.append(extract('algo2', input))

print(algo2)