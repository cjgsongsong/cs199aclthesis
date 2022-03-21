from classes import Poset, LinearOrder, Relations
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

def subtract(rels1: Relations, rels2: Relations):
    rels = []
    for rel in rels1:
        if rel not in rels2:
            rels.append(rel)
    
    return rels

def combinePoset(poset1: Poset, poset2: Poset):
    rels1 = poset1.relations
    rels2 = poset2.relations

    if len(rels1) != len(rels2):
        return Poset([])
    
    rels3 = subtract(rels1, rels2)
    
    if len(rels3) > 1:
        return Poset([])
    
    if len(rels3) == 1:
        (a, b) = rels3[0]
        if (b, a) not in rels2:
            return Poset([])
        
    rels = [rel for rel in rels1 if rel not in rels3]
    return Poset(rels)

def algorithm2(upsilon: list[LinearOrder]):
    PstarRMinusOne = upsilon
    PCurrentFinal = []
    canBeImproved = True

    while canBeImproved:
        canBeImproved = False
        PstarR = []
        for i in range(0, len(PstarRMinusOne) - 1):
            # to check if this is correct
            hasPair = False
            for j in range(i + 1, len(PstarRMinusOne)):
                PstarRK = combinePoset(PstarRMinusOne[i], PstarRMinusOne[j])
                if len(PstarRK.relations) != 0:
                    PstarR.append(PstarRK)
                    hasPair = True
                    canBeImproved = True
            
            if not hasPair:
                PstarRK = PstarRMinusOne[i]
                PstarR.append(PstarRK)

        PCurrentFinal = PstarRMinusOne
        # to check if this is correct
        PstarRMinusOne = PstarR

    return PCurrentFinal