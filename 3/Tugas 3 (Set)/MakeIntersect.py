# Nama file : MakeIntersect.py
# Deskripsi : Membuat himpunan dengan anggota irisan H1 dan H2
# Pembuat   : Aprilyanto Setiyawan Siburian
# NIM       : 24060121120022
# Tanggal   : 07 November 2021

# DEFINISI DAN SPESIFIKASI
# MakeIntersect: 2 set -> set
#   {MakeIntersect(H1,H2) membuat interseksi H1 dengan H2: yaitu set baru dengan anggota elemen
# yang merupakan anggota H1 dan juga anggota H2 atau irisan H1 dan H2}

# IsMember: elemen, list --> boolean
#   {IsMember(x,L) adalah benar jika x adalah elemen list L}

# IsEqual: 2 list -> boolean
#   {IsEqual(L1,L2) benar jika semua elemen list L1 sama dengan L2: sama urutan dan nilainya}

# IsEmpty: list -> boolean
#   {IsEmpty(L1) benar jika list kosong}

# FirstElmt: list tidak kosong -> elemen
#   {FirstElmt(L) menghasilkan elemen pertama list L}

# NbElmt(L) : list --> integer
#   {NbElmt(L) menghasilkan banyaknya elemen list, nol jika kosong}

# Tail : list tidak kosong --> list
#   {Tail(L) menghasilkan list tanpa elemen pertama / nilai pertama, mungkin kosong}

# REALISASI
def Tail(L):
    return L[1:]

def NbElmt(L):
    if L == []:
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
def FirstElmt(L):
    if L != []:
        return L[0]
    
def IsEqual(L1,L2):
    if NbElmt(L1) == NbElmt(L2):
        if L1 == [] and L2 == []:
            return True
        elif FirstElmt(L1) != FirstElmt(L2):
            return False
        else:
            return FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1),Tail(L2))
    else:
        return False

def IsEmpty(L):
    return L==[]

def IsMember(x,L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L)==x:
            return True
        else:
            return IsMember(x,Tail(L))
        
def MakeIntersect(H1,H2):
    if IsEqual(H1,H2):
        return H1
    elif IsEmpty(H1):
        return []    
    else:
        if IsMember(FirstElmt(H1), H2):
            return [FirstElmt(H1)] + MakeIntersect(Tail(H1), H2)
        else:
            return MakeIntersect(Tail(H1), (H2))

#Aplikasi
S1 = [8,4,2,1,5,6,7,11,13]
S2 = [13,9,0,1,2,7]
print(MakeIntersect(S1,S2))
