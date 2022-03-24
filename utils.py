from classes import LinearOrder

def preprocess(input, toLO = True):
    input = input.strip('\n')
    
    if not toLO:
        return input
    else:
        inputSet = []
        for lo_raw in input.split('-'):
            lo = [int(num) for num
                  in lo_raw.strip('[]').split(',')]
            inputSet.append(LinearOrder(lo))
        
        return inputSet

def split(txt):
    data = []
    idx_i = 0
    for idx in range(len(txt)):
        if txt[idx] == '\n':
            data.append(txt[idx_i:idx])
            idx_i = idx + 1
    
    return data

def _get_value(entry):
    return entry.strip('\n').split(':')[1][1:]

def extract(keyword, data_raw):
    data = {}
    if 'algo' in keyword:
        ref_idx = 1
        data[f'runtime_{keyword}'] = float(_get_value(data_raw[ref_idx - 1]).split(' ')[0])
    elif keyword == 'optsol':
        ref_idx = 0
    
    data['input'] = _get_value(data_raw[ref_idx])
    data[f'cost_{keyword}'] = int(_get_value(data_raw[ref_idx + 1]))
    data[f'output_{keyword}'] = [preprocess(datum, False) for datum
                                  in data_raw[ref_idx + 3:len(data_raw)]]
    
    return data