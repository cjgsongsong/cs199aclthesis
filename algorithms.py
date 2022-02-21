from asyncio.windows_events import NULL
from types import Poset, LinearOrder

def combinePoset(poset1: Poset, poset2: Poset):
    if len(poset1.relations) != len(poset2.relations):
        return NULL
    
    poset = Poset(poset1.relations - poset2.relations)

    if len(poset.relations) > 1:
        return NULL
    
    if len(poset.relations) == 1:
        (a, b) = poset.relations[0]
        if (b, a) not in poset2.relations:
            return NULL
    
    return poset

def algorithm2(upsilon: list[LinearOrder]):
    PstarR = []
    PstarRMinusOne = upsilon
    r = 1
    canBeImproved = True

    while canBeImproved:
        canBeImproved = False
        k = 1

        for i in range(1, len(PstarRMinusOne)):
            hasPair = False
            for j in range(i, len(PstarRMinusOne)):
                PstarRK = combinePoset(PstarRMinusOne[i], PstarRMinusOne[j])
                if len(PstarRK) != 0:
                    PstarR.append(PstarRK)
                    k += 1
                    hasPair = True
                    canBeImproved = True
            
            if not hasPair:
                PstarRK = PstarRMinusOne[i]
                PstarR.append(PstarRK)
        
        r += 1