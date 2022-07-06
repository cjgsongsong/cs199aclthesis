from classes import Poset, LinearOrder

def hasSwapPair(l1, l2):
    for i in range(len(l1)-1):
        if l1[i] == l2[i+1] and l1[i+1] == l2[i]:
            return True
        elif l1[i] == l2[i-1] and l1[i-1] == l2[i]:
            return True
    return False

def swapByPair(el, pair):
    l = el.sequence.copy()
    indexA = l.index(pair[0])
    indexB = l.index(pair[1])
    if abs(indexA-indexB) != 1:
        return []
 
    temp = l[indexA]
    l[indexA] = l[indexB]
    l[indexB] = temp
    return l

def swapByIndex(el, i):
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
    hasPair = False
    for i in range(len(l1)):
        if (i != len(l1)-1) and l1[i] == l2[i+1] and l1[i+1] == l2[i]:
            notSamePos += 1
            (a,b) = (l1[i], l1[i+1])
            hasPair = True
        elif (i != 0) and l1[i] == l2[i-1] and l1[i-1] == l2[i]:
            notSamePos+=1
            continue
        elif l1[i] != l2[i]:
            notSamePos += 1
    if notSamePos == 2 and hasPair:
        return (a,b)
    else:
        return (-1,-1)

def components(upsilonTwo):
    upsilon2 = upsilonTwo.copy()   
    compfin = [[upsilon2[0]]]
    upsilon2.pop(0)
    index = 0
    while upsilon2 != []:
        added = False
        for i in range(len(compfin)):
            for j in compfin[i]:
                (a, b) = swapPair(upsilon2[index],j)
                if (a,b) != (-1, -1):
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

def findLOSwap(l, upsilonTwo, lmbda):
    for i in range(len(upsilonTwo)):
        (a,b) = swapPair(l,upsilonTwo[i])
        if (a,b) != (-1,-1) and upsilonTwo[i] not in lmbda:
            return i, (a,b)
    return -1, (-1,-1)

def setDiff(upsilonOne, lmbda):
    counter = 0
    while len(lmbda) > counter:
        for i in upsilonOne:
            if lmbda[counter].sequence == i.sequence:
                upsilonOne.remove(i)
                counter += 1
                break
    return upsilonOne

def getComparable(A, upsilonTwo, el, n):
    upsilon2 = []
    for i in upsilonTwo:
        upsilon2.append(i.sequence)
    
    for i in range(n-1):
        Lprime = swapByIndex(el, i)
        if Lprime not in upsilon2 and (el.sequence[i], el.sequence[i+1]) not in A:
            A.append((el.sequence[i], el.sequence[i+1]))
    
    tempUpsilon = upsilonTwo.copy()
    for i in tempUpsilon:
        if not all(x in i.relations for x in A):
            upsilonTwo.remove(i)
    return A, upsilonTwo

def getIncomparable(B, upsilonTwo, pair):
    if pair not in B:
        B.append(pair)
        done = False
        removed = []
        while not done:
            done = True
            upsilon2 = []
            for i in upsilonTwo:
                upsilon2.append(i.sequence)

            tempUpsilon = upsilonTwo.copy()
            for l3 in tempUpsilon:
                for p in B:
                    l4 = swapByPair(l3, p)
                    if l4 == []: 
                        continue
                    elif l4 not in upsilon2 and l3 not in removed:
                        removed.append(l3)
                        upsilonTwo.remove(l3)
                        upsilon2.remove(l3.sequence)
                        done = False

    return B, upsilonTwo

def algorithm1(upsilon: list[LinearOrder]):
    Pstar = []
    upsilonOne = upsilon.copy()
    n = len(upsilon[0].vertices)

    while upsilonOne != []:
        ell = upsilonOne[0]

        con_comp = components(upsilonOne.copy())
        upsilonTwo = con_comp[0]
        A = []
        B = []
        
        lmbda =  [ell]
        A, upsilonTwo = getComparable(A, upsilonTwo, ell, n)

        while set(upsilonTwo) != set(lmbda):
            ellOne = lmbda[0]
            l2index = -1
            (a,b) = (-1,-1)
            for i in range(len(lmbda)):
                ellOne = lmbda[i]
                l2index, (a,b) = findLOSwap(ellOne, upsilonTwo, lmbda)
                if l2index != -1:
                    break
            if l2index == -1:
                break
            pair = (a,b)
            ellTwo = upsilonTwo[l2index]
            lmbda.append(ellTwo)
            A, upsilonTwo = getComparable(A, upsilonTwo, ellTwo, n)
            B, upsilonTwo = getIncomparable(B, upsilonTwo, pair)

        PstarK = Poset(n, A)
        Pstar.append(PstarK)
        lmbda = list(set(lmbda))
        upsilonOne = setDiff(upsilonOne, lmbda)

    return Pstar

def combinePoset(poset1: Poset, poset2: Poset):
    if len(poset1.relations) != len(poset2.relations):
        return Poset(-1, [], True)
    
    relations = poset1.subtract(poset2)

    if len(relations) != 1:
        return Poset(-1, [], True)
    
    if len(relations) == 1:
        (a, b) = relations[0]
        if (b, a) not in poset2.relations:
            return Poset(-1, [], True)
        
        size = len(poset1.vertices)
        relations = [relation for relation in poset1.relations if relation != (a, b)]
        return Poset(size, relations)

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
                if PstarRK.relations != None: 
                    PstarR.append(PstarRK)
                    hasPair = True
                    canBeImproved = True
            
            if not hasPair:
                PstarRK = PstarRMinusOne[i]
                PstarR.append(PstarRK)

        PCurrentFinal = PstarRMinusOne
        PstarRMinusOne = PstarR
    
    return PCurrentFinal

def algorithm1i(upsilon: list[LinearOrder]):
    pass

def algorithm2i(upsilon: list[LinearOrder]):
    Pstar = upsilon
    PApprox = []
    canBeImproved = True
    while canBeImproved:
        canBeImproved = False
        
        while len(Pstar) > 0:
            poset1 = Pstar[0]
            Pstar.pop(0)
            haspair = False
            for i in range(len(Pstar)):
                PstarRK = combinePoset(poset1, Pstar[i])
                if PstarRK.relations != None:
                    PApprox.append(PstarRK)
                    Pstar.pop(i)
                    haspair = True
                    canBeImproved = True
                    break

            if not haspair:
                PApprox.append(poset1)

        Pstar = PApprox.copy()
        PApprox = []   

    return Pstar