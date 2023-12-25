# Nama file: elemenkeN.py
# Deskripsi: untuk menghasilkan elemen ke-N dari List L
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 31 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# ElmtKeN : integer >= 0, List tidak kosong --> elemen
#  {ElmtKeN(N,L) menghasilkan elemen ke-N list L, N >= 0, dan N <= banyaknya elemen list}

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
    
def ElmtKeN(N,L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtKeN(prec(N), tail(L))

# APLIKASI
L1 = [2,4,1,"er"]
L2 = [1,2,10,"cd","css"]
print(ElmtKeN(4,L1))
print(ElmtKeN(3,L2))
print(ElmtKeN(1,L1))