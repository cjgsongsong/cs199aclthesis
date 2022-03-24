import csv, fileinput
from utils import preprocess, split, extract

#verifier here

#fileInput = open(f"inputs/{args[1]}vertices{args[2]}.txt", "r")
#inputs = fileInput.readlines()
#fileInput.close()

fileInput = open("algo2/3valgo2.txt", "r")
inputs = fileInput.readlines()
fileInput.close()

algo2 = []
for input in split(inputs):
    if len(input) != 1:
        algo2.append(extract('algo2', input))

keys = algo2[0].keys()
with open('results/algo2.csv', 'w', newline='') as fileOutput:
    dw = csv.DictWriter(fileOutput, keys)
    dw.writeheader()
    dw.writerows(algo2)