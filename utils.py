from classes import LinearOrder

def preprocess(input, toLO = True):
    input = input.strip('\n')
    
    if not toLO:
        return input
    else:
        inputSet = []
        for lo_raw in input.split('-'):
            lo = [int(num) for num in lo_raw.strip('[]').split(',')]
            inputSet.append(LinearOrder(lo))
        
        return inputSet