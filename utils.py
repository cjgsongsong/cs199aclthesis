import fileinput
from classes import Poset, LinearOrder

def read(filepath):
    fileInput = open(filepath, "r")
    inputs = fileInput.readlines()
    fileInput.close()

    return inputs

def remove(string, chars):
    for char in chars:
        string = string.replace(char, "")
        
    return string

def preprocess(input, toLO = True, toPoset = False):
    input = input.strip("\n")
    
    if toLO:
        inputSet = []
        for lo_raw in input.split("-"):
            lo = [int(num) for num
                  in lo_raw.strip("[]").split(",")]
            inputSet.append(LinearOrder(lo))
        
        return inputSet
    elif toPoset:
        inputRels = []
        for rel in input.split("(")[1:]:
            a, b = rel.split(",")[:2]
            inputRels.append((int(a), int(remove(b, " ),]"))))
        
        return inputRels
    else:
        return input

def split(txt):
    data = []
    idx_i = 0
    for idx in range(len(txt)):
        if txt[idx] == "\n":
            data.append(txt[idx_i:idx])
            idx_i = idx + 1
    
    return data

def _get_value(entry):
    return entry.strip("\n").split(":")[1][1:]

def verify(input, output):
    upsilon = [lo.sequence for lo in preprocess(input)]
    
    ell = []
    for rels in output:
        poset = Poset(preprocess(rels, False, True))
        for le in poset.generateLinearExtensions():
            if le not in ell:
                ell.append(le)
    
    return sorted(upsilon) == sorted(ell)

def extract(keyword, data_raw, ref_idx = 1):
    data = {}
    
    data["input"] = _get_value(data_raw[ref_idx])

    data[f"cost_{keyword}"] = int(_get_value(data_raw[ref_idx + 1]))
    data[f"output_{keyword}"] = [preprocess(datum, False) for datum
                                 in data_raw[ref_idx + 3:len(data_raw)]]
    
    data[f"runtime_{keyword}"] = float(_get_value(data_raw[ref_idx - 1]).split(' ')[0])

    return data