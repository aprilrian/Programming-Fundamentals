"""
NIM         : 24060121120022
Nama        : Aprilyanto Setiyawan Siburian
Deskripsi   : Fungsi dari soal UAS 2019/2020
Tanggal     : 6 Desember 2021
"""

# 1
def empty_list(L):
    return L == []

def first_element(L):
    return L[0]

def tail(L):
    return L[1:]

# DEFINISI, SPESIFIKASI, REALISASI
# max2 : integer, integer --> integer
#   {max2(a,b) mengeluarkan integer maksimum dari integer a 
# dan b}

def max2(a,b):
    if a > b:
        return a
    else:
        return b

# min2 : integer, integer --> integer
#   {min2(a,b) mengeluarkan integer minimum dari integer a 
# dan b}

def min2(a,b):
    if a > b:
        return b
    else:
        return a

# max_list : list --> elemen
#   {max_list(L) mengeluarkan elemen maksimum dari list L}

def max_list(L):
    if empty_list(L):
        return 0
    else:
        if first_element(L) > max_list(tail(L)):
            return first_element(L)
        else:
            return max_list(tail(L))

# min_list : list --> elemen
#   {min_list(L) mengeluarkan elemen minimal dari list L}

def min_list(L):
    if empty_list(L):
        return 0
    else:
        if first_element(L) < min_list(tail(L)):
            return first_element(L)
        else:
            return min_list(tail(L))

# APLIKASI
L = [9,2,5,1,4,-3,10,-9,1]
print(max_list(L))
print(min_list(L))

# 2
def makePB(akar, left, right):
    return [akar, left, right]

def akar(P):
    return P[0]

def left(P):
    return P[1]

def right(P):
    return P[2]

def is_one_element(P):
    if not P == None and left(P) == None and right(P) == None:
        return True
    else:
        return False
    
def is_uner_left(P):
    if (not P == None) and not (left(P) == None) and (right(P) == None):
        return True
    else:
        return False

def is_uner_right(P):
    if not (P == None) and (left(P) == None) and not (right(P) == None):
        return True
    else:
        return False

def is_biner(P):
    if not (P == None) and not (left(P) == None) and not (right(P) == None):
        return True
    else: 
        return False

# DEFINISI, SPESIFIKASI, REALISASI
# total_elemen_daun : pohon --> integer
#   {total_elemen_daun(P) mengeluarkan jumlah seluruh elemen
# daun pohon P}

def total_elemen_daun(P):
    if is_one_element(P):
        return akar(P)
    else:
        if is_biner(P):
            return total_elemen_daun(left(P)+right(P))
        elif is_uner_left(P):
            return total_elemen_daun(left(P))
        elif is_uner_right(P):
            return total_elemen_daun(right(P))

# total_elemen_node : pohon --> integer
#   {total_elemen_node(P) mengeluarkan jumlah seluruh elemen
# node termasuk akar dari pohon P}

def total_elemen_node(P):
    if is_one_element(P):
        return akar(P)
    else:
        if is_biner(P):
            return total_elemen_node(left(P)) + akar(P) + total_elemen_node(right(P))
        elif is_uner_left(P):
            return total_elemen_node(left(P)) + akar(P)
        elif is_uner_right(P):
            return total_elemen_node(right(P)) + akar(P)

# APLIKASI
P = makePB(8,makePB(3,1,makePB(6,4,7)),makePB(10,None,makePB(14,13,None)))
print(total_elemen_daun(P))
print(total_elemen_node(P))

#3

def empty_list(L):
    return L == []

def first_elmt(L):
    return L[0]

def tail(L):
    return L[1:]

def konso(e,L):
    if L == []:
        return [e]
    else:
        return [e]+L

# DEFINISI, SPESIFIKASI, REALISASI
# Filter_List : List integer, predikat --> List
#   {FilterList (L,f) menghasilkan sebuah list integer dengan 
# elemen yang memenuhi Predikat f dari list Li}}

def Filter_List(L,f):
    if L == []:
        return []
    elif f(first_element(L)):
        return konso(first_element(L),Filter_List(tail(L,f)))
    else:
        return Filter_List(tail(L),f)

# is_genap : integer --> boolean
#   {is_genap(i) bernilai True jika i % 2 = 0}

def is_genap(i):
    return (i % 2) == 0

# is_ganjil : integer --> boolean
#   {is_ganjil(i) bernilai True jika i % 2 ≠ 0}

def is_ganjil(i):
    return (i % 2) != 0

L1 = [4,8,11,2,19,23,45,20]
L2 = Filter_List(L1,is_genap)
L3 = Filter_List(L1,is_ganjil)
L2_lambda = Filter_List(L1, lambda x:x % 2 == 0)
L3_lambda = Filter_List(L1, lambda x:x % 2 != 0)

# 4
# DEFINISI, SPESIFIKASI, REALISASI

def is_member(x, L):
    if L == []:
        return False
    else:
        if first_element(L) == x:
            return True
        else:
            return is_member(x, tail(L))

def minus(L1,L2):
    if L1 == []:
        return []
    else:
        if is_member(L1[0], L2):
            return minus(L1[1:], L2)
        else:
            return [L1[0]] + minus(L1[1:],L2)
