def is_empty(S):
    return S == []

def first(S):
    return S[0]

def tail(S):
    return S[1:]

def nb_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def isOne(L):
    if L == 0:
        return False
    elif nb_element(L)==1:
        return True
    else:
        False

def is_list(S):
    if type(S) == list:
        return True
    else:
        return False

#====================================================================
def makePB(root, left, right):
    return [root, left, right]

p1 = makePB(
    5,
    makePB(3, makePB(2,None,None), makePB(4, None, None)),
    makePB(7, makePB(6, None, None), makePB(8,None,None))
)
def root(P):
    return P[0]

def left(P):
    return P[1]

def right(P):
    return P[2]

def istreeEmpty(P):
    if P == None:
        return True
    else:
        return False

def isOneElmt(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False
    
def isUnerLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False

def isUnerRight(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def isbiner(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else: 
        return False

def isExistLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)):
        return True
    else:
        return False

def isExistRight(P):
    if not istreeEmpty(P) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def NbElmt(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1 
    else:
        if isbiner(P):
            return NbElmt(left(P)) + 1 + NbElmt(right(P))
        elif isUnerLeft(P):
            return NbElmt(left(P)) + 1
        elif isUnerRight(P):
            return NbElmt(right(P)) +1
        else:
            return 0

def NbELmt1(P): 
    if istreeEmpty(P): 
        return 0 
    else: 
        return 1 + NbELmt1(left(P)) + NbELmt1(right(P))

def repPrefix(P):
    if isOneElmt(P):
        return [root(P)]
    else:
        if isbiner(P):
            return [root(P)] + [repPrefix(left(P))] + [repPrefix(right(P))]
        elif isUnerLeft(P):
            return [root(P)] + [repPrefix(left(P))]
        elif isUnerRight(P):
            return [root(P)] + [repPrefix(right(P))]
print(repPrefix(p1))
def NbDaun(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1
    else:
        if isbiner(P):
            return NbDaun(left(P)) + NbDaun(right(P))
        elif isUnerLeft(P):
            return NbDaun(left(P))
        elif isUnerRight(P):
            return NbDaun(right(P))
        else:
            return 0
print(NbDaun(p1))