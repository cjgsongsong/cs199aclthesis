import fileinput
from utils import preprocess

fileInput = open("algo2/3valgo2.txt", "r")
inputs = fileInput.readlines()
fileInput.close()

count = 1
#for input in inputs:
#    if input[0] == "S":
#        continue

#    print(count)
#    count += 1

print(inputs)

#print("FINISH")