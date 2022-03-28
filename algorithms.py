from classes import Poset, LinearOrder
from itertools import chain, combinations

def swapByPair(el, pair):
    l = el.sequence
    indexA = l.index(pair[0])
    indexB = l.index(pair[1])
    if abs(indexA-indexB) == 1:
        temp = l[indexA]
        l[indexA] = l[indexB]
        l[indexB] = temp

    return l

def swapbyIndex(el, i):
    l = el.sequence
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp

    return l

def swapPair(ellone, elltwo):
    l1 = ellone.sequence
    l2 = elltwo.sequence
    notSamePos = 0
    (a,b) = (-1,-1)
    for i in range(len(l1)-1):
        if l1[i] == l2[i+1] and l1[i+1] == l2[i]:
            notSamePos += 1
            (a,b) = (l1[i], l1[i+1])
        elif l1[i] == l2[i-1] and l1[i-1] == l2[i]:
            notSamePos += 1
        elif l1[i] != l2[i]:
            notSamePos += 1
    if notSamePos == 2:
        return (a,b) #(a,b) is the swap pair
    else:
        return (-1,-1) #means ellone and elltwo don't have "swap pair"

def getComparable(A, upsilonTwo, el, n):
    upsilon2 = [] #will be used for "not in" conditional
    for i in upsilonTwo:
        upsilon2.append(i.sequence)
    
    for i in range(n-1):
        Lprime = swapbyIndex(el, i)
        if Lprime not in upsilon2:
            A.append((el[i], el[i+1]))
    
    tempUpsilon = upsilonTwo.copy()
    for i in tempUpsilon:
        if all(x in i.relations for x in A):
            upsilonTwo.remove(i)

def getIncomparable(B, upsilonTwo, ellone, elltwo):
    (a,b) = swapPair(ellone, elltwo)
    pair = (a,b)

    upsilon2 = [] #will be used for "not in" conditional
    for i in upsilonTwo:
        upsilon2.append(i.sequence)

    tempUpsilon = upsilonTwo.copy()
    if pair not in B:
        B = B.append(pair)
        for l3 in tempUpsilon:
            l4 = swapByPair(l3, pair)
            if l4 not in upsilon2:
                upsilonTwo.remove(l3)
                upsilon2.remove(l3.sequence)

def algorithm1(upsilon: list[LinearOrder], n):
    Pstar = []
    k = 1
    upsilonOne = upsilon.copy()

    while upsilonOne != []:
        # select L in upsilonOne
        ell = upsilonOne[0]
        ellOne = upsilonOne[0]
        ellTwo = upsilonOne[1]

        upsilonTwo = upsilon.copy() # set of linear orders in connected component of G(Y') that contains L
        A = []
        B = []
        lmbda =  [ell]
        (A, upsilonTwo) = getComparable(A, upsilonTwo, ellTwo, n)

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

    if len(relations) != 1:
        return Poset([])
    
    if len(relations) == 1:
        (a, b) = relations[0]
        if (b, a) not in poset2.relations:
            return Poset([])
        
        relations = [relation for relation in poset1.relations if relation not in relations]
        return Poset(relations)

def algorithm2(upsilon: list[LinearOrder]):
    PstarR = []
    PstarRMinusOne = upsilon
    PCurrentFinal = []
    canBeImproved = True

    while canBeImproved:
        canBeImproved = False
        PstarR = []
        for i in range(0, len(PstarRMinusOne) - 1):
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
        PstarRMinusOne = PstarR
    
    return PCurrentFinal