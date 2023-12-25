# Nama file: is_inverse.py
# Deskripsi: untuk mengecek apakah suatu list adalah list dengan urutan elemen terbalik dibandingan suatu list lain
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 31 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# IsInverse : 2 list --> boolean
#   {IsInverse(L1,L2) true jika L2 adalah list dengan urutan elemen terbalik dari L1}

# FirstElmt : List tidak kosong --> elemen
#   {FirstElmt(L) menghasilkan elemen pertama list L}

# LastElmt : list tidak kosong --> elemen
#   {LastElmt(L) mengeluarkan elemen terakhir list L}

# is_empty : List --> boolean
#   {is_empty(L) benar jika list kosong}

# NbElmt(L) : list --> integer
#   {NbElmt(L) menghasilkan banyaknya elemen list, nol jika kosong}

# head : list tidak kosong --> list
#   {head(L) menghasilkan list tanpa elemen terakhir list L, mungkin kosong}

# tail : List tidak kosong --> List
#   {tail(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong}

# REALISASI
def tail(L):
    if not (is_empty(L)):
        return L[1:]
    
def head(L):
    if not(is_empty(L)):
        return L[:-1]
    
def NbElement(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NbElement(tail(L))
    
def is_empty(L):
    return L==[]

def FirstElmt(L):
    if not (is_empty(L)):
        return L[0]
    
def LastElmt(L):
    if not(is_empty(L)):
        return L[-1]
    
def IsInverse(L1,L2):
    if NbElement(L1)==NbElement(L2):
        if is_empty(L1) and is_empty(L2):
            return True
        else:
            return FirstElmt(L1)==LastElmt(L2) and IsInverse((head(tail(L1))),(head(tail(L2))))
    else:
        return False

# APLIKASI
R1 = [2,4,1,3]
R2 = [1,2,10,"cd","css"]
R3 = [3,1,4,2]
print(IsInverse(R2,R1))
print(IsInverse(R3,R1))