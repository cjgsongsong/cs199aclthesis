import fileinput
from classes import Poset, LinearOrder

def isAllConnected(vertices, relations):
    for vertex in vertices:
        isConnected = False
        for relation in relations:
            if vertex in relation:
                isConnected = True
                break
        
        if not isConnected: return False
    
    return True

def generateRootedRelations(parent, vertices, relations):
    if len(vertices) == 0:
        return [sorted(relations)]
    else:
        rels = []
        for child in vertices:
            newVertices = [v for v in vertices if v != child]
            rels.extend(generateRootedRelations(parent, newVertices, relations + [(parent, child)]))
            rels.extend(generateRootedRelations(parent, newVertices, relations + [(child, parent)]))
            rels.extend(generateRootedRelations(child, newVertices, relations + [(parent, child)]))
            rels.extend(generateRootedRelations(child, newVertices, relations + [(child, parent)]))
        
        truerels = []
        for rel in rels:
            if rel not in truerels: truerels.append(rel)

        return truerels

def read(filepath):
    fileInput = open(filepath, "r")
    inputs = fileInput.readlines()
    fileInput.close()

    return inputs

def remove(string, chars):
    for char in chars:
        string = string.replace(char, "")
        
    return string

def preprocess(input, toLO = True, toPoset = False, toList = False):
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
    elif toList:
        lst = []
        for elem in input.split('\'')[1:-1]:
            if '[' in elem:
                lst.append(elem)
        
        return lst        
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

def extract(keyword, data_raw, ref_idx = 1):
    data = {}
    
    data["input"] = _get_value(data_raw[ref_idx])

    data[f"cost_{keyword}"] = int(_get_value(data_raw[ref_idx + 1]))
    data[f"output_{keyword}"] = [preprocess(datum, False) for datum
                                 in data_raw[ref_idx + 3:len(data_raw)]]
    
    if ref_idx == 1:
        data[f"runtime_{keyword}"] = float(_get_value(data_raw[ref_idx - 1]).split(' ')[0])

    return data

def getLinearOrders(input):
    return sorted([lo.sequence for lo in preprocess(input)])

def getLinearExtensions(size, output, perPoset = False):
    ell = []
    for rels in output:
        poset = Poset(size, preprocess(rels, False, True))
        if perPoset:            
            ell.append(poset.generateLinearExtensions())
        else:
            for le in poset.generateLinearExtensions():
                if le not in ell:
                    ell.append(le)
    
    if perPoset:
        return ell
    return sorted(ell)

def verify(input, output, shouldLog = False):
    upsilon = getLinearOrders(input)
    ell = getLinearExtensions(len(upsilon[0]), output)
    
    if shouldLog:
        print(input)
        print(output)
        print("-----")
        print(upsilon)
        print(ell)

    return upsilon == ell


def countInversions(lo_input):
    count = 0
    los = [lo.sequence for lo in preprocess(lo_input)]
    for i in range(len(los)):
        lo_ref = los[i]
        for j in range(i + 1, len(los)):
            lo = [0 for k in range(len(lo_ref))]
            for l in range(len(lo_ref)):
                lo[los[j].index(lo_ref[l])] = l
            
            count += sum(pi > lo[j]
                         for i, pi in enumerate(lo)
                         for j in range(i + 1, len(lo)))
    
    return count

def countSwapPairs(lo_input):
    count = 0
    los = [lo.relations for lo in preprocess(lo_input)]
    for i in range(len(los)):
        lo_ref = sorted(los[i])
        for j in range(i + 1, len(los)):
            lo = sorted([(b, a) for a, b in los[j]])
            count += len(set(lo_ref).intersection(set(lo)))
    
    return count

def countVertices(lo_input):
    return lo_input.split('-')[0].count(',') + 1