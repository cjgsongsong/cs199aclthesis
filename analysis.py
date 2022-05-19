import csv, sys
from utils import read, split, extract, verify

keywords = ["algo1", "algo2", "optsol"]

args = sys.argv[1:]
if len(args) == 1:
    args.append("")

for keyword in keywords:
    if keyword == "optsol" and args[1] != "": continue

    if args[1] == "":
        inputs = read(f"{keyword}/{args[0]}v{keyword}.txt")
    else:
        inputs = read(f"{keyword}/{args[1]}/{args[0]}v{keyword}.txt")

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
        with open(f'results/{args[0]}v{keyword}{args[1]}.csv', 'w', newline='') as fileOutput:
            dw = csv.DictWriter(fileOutput, keys)
            dw.writeheader()
            dw.writerows(dictlist)

print('FINISH')