# Nama file : MakeUnion.py
# Deskripsi : Membuat himpunan dengan anggota irisan H1 dan H2
# Pembuat   : Aprilyanto Setiyawan Siburian
# NIM       : 24060121120022
# Tanggal   : 07 November 2021

# DEFINISI DAN SPESIFIKASI
# MakeUnion: 2 set -> set
#   {MakeUnion(H1,H2) membuat union H1 dengan H2: yaitu set baru dengan semua anggota elemen H1 dan 
#    anggota H2}

# IsEqual: 2 list -> boolean
#   {IsEqual(L1,L2) benar jika semua elemen list L1 sama dengan L2: sama urutan dan nilainya}

# IsEmpty: list -> boolean
#   {IsEmpty(L1) benar jika list kosong}

# IsMember: elemen, List --> boolean
#   {IsMember(x,L) adalah benar jika x adalah elemen list L}

# FirstElmt: list tidak kosong -> elemen
#   {FirstElmt(L) menghasilkan elemen pertama list L}

# MultiRember: elemen, list -> list
#   {MultiRember(x,L) menghapus setiap elemen x dari list}

# Konso : elemen, list -> list
#	{Konso(e,L) menghasilkan sebuah list dari L dengan menambahkan e sebagai elemen pertama}

# MakeSet: list -> set
#   {MakeSet(L) membuat set dari sebuah list atau membuang semua kemunculan elemen yang lebih dari sekali}

# NbElmt(L) : list --> integer
#   {NbElmt(L) menghasilkan banyaknya elemen list, nol jika kosong}

# Tail : list tidak kosong --> list
#   {Tail(L) menghasilkan list tanpa elemen pertama / nilai pertama, mungkin kosong}

#Realisasi
def Tail(L):
    if not (IsEmpty(L)):
        return L[1:]
    
def NbElmt(L):
    if L == []:
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
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

def FirstElmt(L):
	return L[0]

def IsMember(x, L):
    if IsEmpty(L) == True:
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            return IsMember(x, Tail(L))
        
def MakeSet(L):
    if IsEmpty(L):
        return L
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmt(L),MakeSet(Tail(L)))
        
def Konso(e,L):
    if L==[]:
        return [e]
    else:
        return [e] + L
    
def MakeUnion(H1,H2):
    if IsEqual(H1,H2):
        return H1
    elif (IsEmpty(H1) and IsEmpty(H2)):
        return []
    else:
        if IsEmpty(H1):
            return H2
        elif IsEmpty(H2):
            return H1
        elif IsMember(FirstElmt(H1), H2):
            return MakeSet([FirstElmt(H1)] + MakeUnion(Tail(H1),Tail(H2)))
        elif not IsMember(FirstElmt(H1), H2):
            return MakeSet([FirstElmt(H1)] + [FirstElmt(H2)] + MakeUnion(Tail(H1),Tail(H2)))

#Aplikasi
S1 = [8,4,2,1,5,6,7,11,13]
S2 = [13,9,0,1,2,7]
print(MakeUnion(S1,S2))
