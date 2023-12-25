"""
NIM         : 24060121120022
Nama        : Aprilyanto Setiyawan Siburian
Deskripsi   : Implementasi beberapa fungsi yang berhubungan dengan LoL (List of List)
Tanggal     : 15 November 2021
"""
"""Ex:
Matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
Matrix1 = [
              [1,2,3],
              [4,5,6],
              [7,8,9]
              ]
"""
# Modul List
def isEmpty(L):
    return L == []

def isOneElmt(L):
    return NbElement(L) == 1

def FirstElmt(L):
    if not(isEmpty(L)):
        return L[0]

def tail(L):
    if not(isEmpty(L)):
        return L[1:]

def NbElement(L: list):
    if isEmpty(L):
        return 0
    else:
        return 1 + NbElement(tail(L))

# Modul LoL (List of List)
def isEmpty(S):
    return S == []

def isAtom(S):
    return not(isEmpty(S)) and not(isList(S))

def isList(S):
    return type(S) == list

def konsoLoL(L, S):
    if isEmpty(S):
        return [L]
    else:
        return [L] + S

def Max2(a,b):
    if a>=b:
        return a
    else :
        return b

# 1
# DefSpek
# NbEleX : elemen, list of list --> integer
# NbEleX (L,X) menentukan banyaknya X dalam list L
# L1 = [[4], 2, [3,4], 1, 4]
# aplikasi : NbEleX(L1,4) --> 3 
def NbEleSubX(L, X):
    if isEmpty(L) == True:
        return 0
    else:
        if FirstElmt(L) == X:
            return NbEleSubX(tail(L), X) + 1
        else:
            return NbEleSubX(tail(L), X)

def NbEleX(L, X):
    if isEmpty(L) == True:
        return 0
    else:
        if isList(FirstElmt(L)) == True:
            return NbEleSubX(FirstElmt(L), X) + NbEleX(tail(L), X)
        elif isAtom(FirstElmt(L)) == True:
            if FirstElmt(L) == X:
                return NbEleX(tail(L), X) + 1
            else:
                return NbEleX(tail(L), X)
        else:
            return NbEleX(tail(L), X)

# 2
# DefSpek
# KaliMatrix : Integer, list of list dalam bentuk matrix --> list
# KaliMatrix (k, L) menghasilkan matrix dalama bentuk list
# yang telah dikali dengan suatu konstanta K
# L3 = [[1,2,3], [4,5,6], [7,8,9]]
# aplikasi : KaliMatrix(2, L3) --> [[2,4,6],[8,10,12],[14,16,18]]
def EleTimesX(x, L):
    if isEmpty(L) == True:
        return []
    else:
        return konsoLoL(FirstElmt(L) * x, EleTimesX(x, tail(L)))

def KaliMatrix(k, L):
    if isEmpty(L) == True:
        return []
    else:
        if isList(FirstElmt(L)) == True:
            return konsoLoL(EleTimesX(k, FirstElmt(L)), KaliMatrix(k, tail(L)))
        else:
            return konsoLoL(FirstElmt(L) * 2, KaliMatrix(k, tail(L)))

# 3
# DefSpek
# NbList : list of list --> integer
# NbList (L) menghitung jumlah list dalam list L
# L4 = [1, [2,3], [4]]
# L3 = [[5], [6], [7]]
# L2 = [8, 9, 10]
# aplikasi : NbList(L4) --> 2
#               NbList(L3) --> 3
#               NbList(L2) --> 0
def NbList(L):
    if isEmpty(L) == True:
        return 0
    else:
        if isList(FirstElmt(L)) == True:
            return NbList(tail(L)) + 1 
        else:
            return NbList(tail(L))
        
# Aplikasi
L1 = [[4], 2, [3,4], 1, 4]
L2 = [[1,2,3], [4,5,6], [7,8,9]]
L3 = [1, [2,3], [4]]
L4 = [[5], [6], [7]]
L5 = [8, 9, 10]
print(NbEleX(L1,4))
print(KaliMatrix(2, L3))
print(NbList(L3))
print(NbList(L4))
print(NbList(L5))