import csv
from utils import read, split, extract

#verifier here

keywords = ['algo2', 'optsol']

for keyword in keywords:
    inputs = read(f"{keyword}/3v{keyword}.txt")
    for splice in range(1, 5):
        inputs += read(f"{keyword}/4v{splice}{keyword}.txt")

    dictlist = []
    for input in split(inputs):
        if len(input) != 1:
            dictlist.append(extract(keyword, input))

    keys = dictlist[0].keys()
    with open(f'results/{keyword}.csv', 'w', newline='') as fileOutput:
        dw = csv.DictWriter(fileOutput, keys)
        dw.writeheader()
        dw.writerows(dictlist)