import csv, sys
from utils import read, split, extract

#verifier here

keywords = ['algo2', 'optsol']

vmax = int(sys.argv[1])
for keyword in keywords:
    inputs = []
    for v in range(3, vmax + 1):
        inputs += read(f"{keyword}/{v}v{keyword}.txt")

    dictlist = []
    for input in split(inputs):
        if len(input) != 1:
            dictlist.append(extract(keyword, input))

    keys = dictlist[0].keys()
    with open(f'results/{keyword}.csv', 'w', newline='') as fileOutput:
        dw = csv.DictWriter(fileOutput, keys)
        dw.writeheader()
        dw.writerows(dictlist)