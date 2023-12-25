# Nama file : ListofList.py
# Deskripsi : Implementasi beberapa fungsi dan predikat yang berhubungan dengan LoL (List of List)
# Pembuat   : Aprilyanto Setiyawan Siburian
# NIM       : 24060121120022
# Tanggal   : 14 November 2021

# DEFINISI DAN SPESIFIKASI
# IsEqS : 2 List of list --> boolean
#   {IsEqS(S1,S2) true jika S1 identik dengan S2: semua elemennya sama}

# IsMemberS : elemen, List of list --> boolean
#   {IsMemberS (a,S) true jika a adalah anggota S}

# IsMemberLS : List, List of list --> boolean
#   {IsMemberLS (L,S2) true jika L adalah anggota S}

# Rember : elemen, List of list --> List of list
#   {Rember(a,S) menghapus sebuah elemen bernilai a dari semua list S}

# Max : List of list tidak kosong --> integer
#   {Max(S) menghasilkan nilai elemen (atom) yang maksimum dari S}

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

# REALISASI
def IsEqS(S1, S2):
    if isEmpty(S1) == True and isEmpty(S2) == True:
        return True
    elif (isEmpty(S1) == True and isEmpty(S2) == False) or (isEmpty(S1) == False and isEmpty(S2) == True):
        return False
    else:
        if isAtom(FirstElmt(S1)) and isAtom(FirstElmt(S2)):
            return FirstElmt(S1) == FirstElmt(S2) and IsEqS(tail(S1), tail(S2))
        elif isList(FirstElmt(S1)) and isList(FirstElmt(S2)):
            return IsEqS(FirstElmt(S1), FirstElmt(S2)) and IsEqS(tail(S1), tail(S2))
        else:
            return False

def IsMemberS(A, S):
    if isEmpty(S) == True:
        return False
    else:
        if isAtom(FirstElmt(S)):
            return A == FirstElmt(S) or IsMemberS(A, tail(S))
        elif isList(FirstElmt(S)):
            return IsMemberS(A, FirstElmt(S)) or IsMemberS(A, tail(S))

def IsMemberLS(L, S):
    if isEmpty(L) == True and isEmpty(S) == True:
        return True
    elif (isEmpty(L) == False and isEmpty(S) == True) or (isEmpty(L) == True and isEmpty(S) == False):
        return False
    else:
        if isAtom(FirstElmt(S)):
            return IsMemberLS(L, tail(S))
        else:
            if IsEqS(L, FirstElmt(S)) == True:
                return True
            else:
                return IsMemberLS(L, tail(S))

def Rember(a, S):
    if isEmpty(S):
        return S
    else:
        if isList(FirstElmt(S)):
            return konsoLoL(Rember(a, FirstElmt(S)), Rember(a, tail(S)))
        else:
            if FirstElmt(S) == a:
                return Rember(a, tail(S))
            else:
                return konsoLoL(FirstElmt(S), Rember(a, tail(S)))

def Max(S):
    if isOneElmt(S):
        if isAtom(FirstElmt(S)):
            return FirstElmt(S)
        else:
            return Max(FirstElmt(S))
    else:
        if isAtom(FirstElmt(S)):
            return Max2(FirstElmt(S), Max(tail(S)))
        else:
            return Max2(Max(FirstElmt(S)), Max(tail(S)))

# Aplikasi
L1 = [[1,2,3],4,[5,6]]
L2 = [[1,2,3],4,5,[6]]
print(IsEqS(L1,L1))
print(IsEqS(L1,L2))
print(IsMemberS(4,L1))
print(IsMemberS(7,L1))
print(IsMemberLS([1,2,3],L1))
print(IsMemberLS([6],L1))
print(Rember(1,L1))
print(Max(L1))