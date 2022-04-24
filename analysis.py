import csv, sys
from utils import read, split, extract, verify, getLinearOrders, getLinearExtensions

keywords = ["algo1", "algo2", "optsol"]

vmax = int(sys.argv[1])
for keyword in keywords:
    inputs = []
    for v in range(3, vmax + 1):
        inputs += read(f"{keyword}/{v}v{keyword}.txt")

    dictlist = []
    isAllCorrect = True
    for input in split(inputs):
        if len(input) != 1:
            d = extract(keyword, input)
            if verify(d["input"], d[f"output_{keyword}"]):
                dictlist.append(d)
            else:
                isAllCorrect = False
                print(f"Incorrect solution detected from {keyword}!")
                verify(d["input"], d[f"output_{keyword}"], True)
                break

    if isAllCorrect:
        keys = dictlist[0].keys()
        with open(f'results/{keyword}.csv', 'w', newline='') as fileOutput:
            dw = csv.DictWriter(fileOutput, keys)
            dw.writeheader()
            dw.writerows(dictlist)

print('FINISH')