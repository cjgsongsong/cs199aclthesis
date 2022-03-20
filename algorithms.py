from classes import Poset, LinearOrder
from itertools import chain, combinations

def getComparable():
    pass

def getIncomparable():
    pass

def algorithm1(upsilon: list[LinearOrder]):
    Pstar = []
    k = 1
    upsilonOne = upsilon

    while upsilonOne != []:
        # select L in upsilonOne
        ell = upsilonOne[0]
        ellOne = upsilonOne[0]
        ellTwo = upsilonOne[1]

        upsilonTwo = upsilon # set of linear orders in connected component of G(Y') that contains L
        A = []
        B = []
        lmbda =  [ellOne]
        (A, upsilonTwo) = getComparable(A, upsilonTwo, ellTwo)

        while upsilonTwo != lmbda:
            # select ellOne in lmbda and ellTwo in upsilonTwo
            # such that ellOne <- ellTwo
            lmbda.append(ellTwo)
            (A, upsilonTwo) = getComparable(A, upsilonTwo, ell)
            (B, upsilonTwo) = getIncomparable(B, upsilonTwo, ellOne, ellTwo)
        
        PstarK = [] # (V, <_Pk) where <_Pk is transitive closure of A 
        Pstar.append(PstarK)
        k += 1
        upsilonOne -= lmbda # set difference

def combinePoset(poset1: Poset, poset2: Poset):
    if len(poset1.relations) != len(poset2.relations):
        return Poset([])
    
    poset = Poset(poset1.relations - poset2.relations)

    if len(poset.relations) > 1:
        return Poset([])
    
    if len(poset.relations) == 1:
        (a, b) = poset.relations[0]
        if (b, a) not in poset2.relations:
            return Poset([])
    
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