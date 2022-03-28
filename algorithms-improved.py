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
    
    relations = poset1.subtract(poset2)
    # print(relations)
    # to check if this correct

    if len(relations) > 1:
        return Poset([])
    
    if len(relations) == 1:
        (a, b) = relations[0]
        if (b, a) not in poset2.relations:
            return Poset([])
        relations = [relation for relation in poset1.relations if relation != (a,b)]
    return Poset(relations)

def algorithm2v2(upsilon: list[LinearOrder]):
    ## the following if-statement is not included in the original algo2 design 

    Pstar = upsilon
    PApprox = []

    while len(Pstar) > 0:
        poset1 = Pstar[0]
        Pstar.pop(0)
        haspair = False
        for i in range(len(Pstar)):
            PstarRK = combinePoset(poset1, Pstar[i])
            if len(PstarRK.relations) != 0:
                PApprox.append(PstarRK)
                Pstar.pop(i)
                haspair = True
                break
        if not haspair:
            PApprox.append(poset1)
            
    return PApprox
    # while canBeImproved:
    #     canBeImproved = False
    #     PstarR = []
    #     for i in range(0, len(PstarRMinusOne) - 1):
    #         hasPair = False
    #         for j in range(i + 1, len(PstarRMinusOne)):
    #             # print(f"nasa {i}, {j} prinoprocess ko") #
    #             #print([i.relations for i in PstarRMinusOne]) #
    #             #print(f"{PstarRMinusOne[i].relations} || {PstarRMinusOne[j].relations}")#
    #             PstarRK = combinePoset(PstarRMinusOne[i], PstarRMinusOne[j])
    #             #PstarRK = Poset([]) #
    #             if len(PstarRK.relations) != 0:
    #                 PstarR.append(PstarRK)
    #                 hasPair = True
    #                 canBeImproved = True
    #                 break
            
    #         if not hasPair:
    #             PstarRK = PstarRMinusOne[i]
    #             PstarR.append(PstarRK)

    #     PCurrentFinal = PstarRMinusOne
    #     PstarRMinusOne = PstarR
    #     if len(PstarRMinusOne) < len (PCurrentMinimal):
    #         PCurrentMinimal = PstarRMinusOne
        