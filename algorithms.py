from classes import Poset, LinearOrder

def hasSwapPair(l1, l2):
    for i in range(len(l1)-1):
        if l1[i] == l2[i+1] and l1[i+1] == l2[i]:
            return True
        elif l1[i] == l2[i-1] and l1[i-1] == l2[i]:
            return True
    return False

def components(upsilonTwo):
    upsilon2 = upsilonTwo.copy()   
    compfin = [[upsilon2[0]]]
    upsilon2.pop(0)
    index = 0
    while upsilon2 != []:
        added = False
        for i in range(len(compfin)):
            for j in compfin[i]:
                if hasSwapPair(upsilon2[index].sequence, j.sequence):
                    compfin[i].append(upsilon2[index])
                    upsilon2.pop(index)
                    added = True
                    index = 0
                    break
            if added:
                break
        if not added:
            index += 1
            if len(upsilon2) <= index:
                compfin.append([upsilon2[0]])
                upsilon2.pop(0)
                index = 0

    return compfin

def swapByPair(el, pair):
    l = el.sequence.copy()
    indexA = l.index(pair[0])
    indexB = l.index(pair[1])
    
    temp = l[indexA]
    l[indexA] = l[indexB]
    l[indexB] = temp
    return l

def swapbyIndex(el, i):
    l = el.sequence.copy()
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp

    return l

def swapPair(ellone, elltwo):
    l1 = ellone.sequence.copy()
    l2 = elltwo.sequence.copy()
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
        return (a,b)
    else:
        return (-1,-1) # no valid swap pair

def findLOswap(l, upsilonTwo, lmbda):
    for i in range(1, len(upsilonTwo)):
        (a,b) = swapPair(l,upsilonTwo[i])
        if (a,b) != (-1,-1) and upsilonTwo[i] not in lmbda:
            return i
    return -1

def getComparable(A, upsilonTwo, el, n):
    upsilon2 = [] # will be used for "not in" conditional
    for i in upsilonTwo:
        upsilon2.append(i.sequence)
    
    for i in range(n-1):
        Lprime = swapbyIndex(el, i)
        if Lprime not in upsilon2:
            A.append((el.sequence[i], el.sequence[i+1]))
    
    tempUpsilon = upsilonTwo.copy()
    for i in tempUpsilon:
        if not all(x in i.relations for x in A):
            upsilonTwo.remove(i)
    return A, upsilonTwo

def getIncomparable(B, upsilonTwo, ellone, elltwo):
    (a,b) = swapPair(ellone, elltwo)
    pair = (a,b)
    
    upsilon2 = [] # will be used for "not in" conditional
    for i in upsilonTwo:
        upsilon2.append(i.sequence)

    tempUpsilon = upsilonTwo.copy()
    
    if pair not in B:
        B.append(pair)
        for l3 in tempUpsilon:
            l4 = swapByPair(l3, pair)
            if l4 not in upsilon2:
                upsilonTwo.remove(l3)
                upsilon2.remove(l3.sequence)
    return B, upsilonTwo

def setDiff(upsilonOne, lmbda):
    counter = 0
    while len(lmbda) > counter:
        for i in upsilonOne:
            if lmbda[counter].sequence == i.sequence:
                upsilonOne.remove(i)
                counter += 1
                break
    return upsilonOne

def algorithm1(upsilon: list[LinearOrder], n):
    Pstar = []
    upsilonOne = upsilon.copy()

    while upsilonOne != []:
        # select L in upsilonOne
        ell = upsilonOne[0]

        con_comp = components(upsilonOne.copy())
        upsilonTwo = con_comp[0] # set of linear orders in connected component of G(Y') that contains L
        A = []
        B = []
        
        lmbda =  [ell]
        A, upsilonTwo = getComparable(A, upsilonTwo, ell, n)
        
        while upsilonTwo != lmbda:
            print("==========================")
            for i in upsilonTwo:
                print(i.sequence)
            print("----------------------------")            
            for i in lmbda:
                print(i.sequence)
            print("==========================")

            ellOne = lmbda[0]
            l2index = findLOswap(ellOne, upsilonTwo, lmbda)
            ellTwo = upsilonTwo[l2index]
            lmbda.append(ellTwo)
            A, upsilonTwo = getComparable(A, upsilonTwo, ellTwo, n)
            if l2index == -1:
                break
            B, upsilonTwo = getIncomparable(B, upsilonTwo, ellOne, ellTwo)
        
        PstarK = Poset(A)
        Pstar.append(PstarK)
        upsilonOne = setDiff(upsilonOne, lmbda)

    return Pstar

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
        
        relations = [relation for relation in poset1.relations if relation != (a, b)]
        return Poset(relations)

def algorithm2(upsilon: list[LinearOrder]):
    PstarR = []
    PstarRMinusOne = upsilon
    PCurrentFinal = []
    canBeImproved = True

    while canBeImproved:
        canBeImproved = False
        PstarR = []
        for i in range(0, len(PstarRMinusOne)):
            hasPair = False
            for j in range(i, len(PstarRMinusOne)):
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

def algorithm1v2(upsilon: list[LinearOrder]):
    pass

def algorithm2v2(upsilon: list[LinearOrder]):
    pass