# Nama file: is_XelemenkeN.py
# Deskripsi: untuk mengecek apakah suatu bilangan integer adalah elemen ke-n dari list L
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 31 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# IsXElmtKeN : elemen, integer >= 0, List tidak kosong --> boolean
#   {IsXElmtKeN(x,n,L) true jika X adalah elemen ke-N dari list L, N >= 0, dan N <= banyaknya elemen list}

# IsMember : elemen, List --> boolean
#   {IsMember(x,L) true jika x adalah elemen dari List L}

# FirstElmt : List tidak kosong --> elemen
#  {FirstElmt(L) menghasilkan elemen pertama list L}

# is_empty : List --> boolean
#   {is_empty(L) benar jika list kosong}

# tail : List tidak kosong --> List
#   {tail(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong}

# prec : integer --> integer
#   {prec(n) adalah representasi maksimal atau minimal n}

# REALISASI
def prec(n):
    return n - 1

def tail(L):
    if not (is_empty(L)):
        return L[1:]
    
def is_empty(L):
    return L == []
    
def FirstElmt(L):
    if not (is_empty(L)):
        return L[0]
    
def IsMember(x,L):
    if is_empty(L):
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            IsMember(x,tail(L))

def IsXElmtKeN(x,n,L):
    if IsMember(x,L):
        if n == 1 and FirstElmt(L) == x:
            return True
        else:
            return False or IsXElmtKeN(x,prec(n),tail(L))
    else:
        return False
    
# APLIKASI
L1 = [2,4,1,"er"]
L2 = [1,2,10,"cd","css"]
print(IsXElmtKeN(2,1,L1))
print(IsXElmtKeN(1,4,L2))
print(IsXElmtKeN(2,1,L2))