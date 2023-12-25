# Nama file : daspro08_24060121120022_Aprilyanto Setiyawan Siburian.py
# Deskripsi : Tugas 8 Praktikum Daspro
# Pembuat   : Aprilyanto Setiyawan Siburian
# Tanggal   : 31 Oktober 2021

def IsEmpty(L):
    return L == []

def FirstElmt(T):
    if not IsEmpty(T):
        return T[0]
    else:
        return []
    
def LastElmt(L):
    if not IsEmpty(L):
        return L[-1]
    else:
        return []
    
def Head(L):
    if not IsEmpty(L):
        return L[:-1]
    else:
        return []
    
def Tail(T):
    if not IsEmpty(T):
        return T[1:]
    else:
        return []
    
def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))
    
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
def Konso(x, l):
	return [x] + l

def Kons(l, x):
	return l + [x]

def Konsa(x, y, l):
	return [y] + [x] + l

def Rember(x, l):
    if IsEmpty(l):
        return []
    elif FirstElmt(l)==x:
        return Tail(l)
    else:
        return Konso(FirstElmt(l), Rember(x, Tail(l)))
    
def IsPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    else:
        return True

L = [3,2,10,5]
L1 = [6,7,1,'t',"non",2]
L2 = [1,"e",33,7,"abc"]

# 0
# DEFINISI DAN SPESIFIKASI
# NbVokal : list of char --> integer
#   {NbVokal(L) menghitung banyak elemen vokal dalam list L}
# REALISASI
def NbVokal(L):
    if IsEmpty(L) == True:
        return 0
    else:
        if IsMember(FirstElmt(L), ['a', 'i', 'u', 'e', 'o']):
            return NbVokal(Tail(L)) + 1
        else:
            return NbVokal(Tail(L))
# APLIKASI
print(NbVokal(L))

# 1
# SumElmt : list of integer --> integer
#   {SumElmt(L) menghasilkan jumlah semua elemen dalam list L}
# REALISASI
def SumElmt(L):
    if IsEmpty(L) == True:
        return 0
    else:
        return SumElmt(Tail(L)) +FirstElmt(L)

# APLIKASI
print(SumElmt([1,3,5,7,10]))

# 2
# KEMUNCULAN MAKSIMUM versi-2
# DEFINISI DAN SPESIFIKASI
# maxNb : list of integer --> <integer, integer>
#   {maxNb(L) menghasilkan <nilai maksimum, kemunculan nilai maksimum> dari suatu list integer L; 
#    <m,n> = m adalah maks x dari n occurence m dalam list L}
#
# max : list of integer --> integer
#   {max(L) menghasilkan nilai maksimum dari elemen suatu list integer L}
#
# Vmax : list of integer --> integer
#   {Vmax(L) adalah NbOcc(max(L),L) yaitu banyaknya kemunculan nilai maksimum dari L, 
#    dengan aplikasi terhadap NbOcc(max(L),L)}
#
# NbOcc : integer, list of integer --> integer > 0
#   {NbOcc(X,L) yaitu banyaknya kemunculan nilai X pada L}
# REALISASI
def maxNbCount(L, max):
    if IsEmpty(L) == True:
        return 0
    else:
        if FirstElmt(L) == max:
            return maxNbCount(Tail(L), max) + 1
        else:
            return maxNbCount(Tail(L), max)
        
def maxNb(L):
    return max(L), maxNbCount(L, max(L))

def max(L):
    if IsEmpty(L) == True:
        return 0
    else:
        return FirstElmt(L) if FirstElmt(L) > max(Tail(L)) else max(Tail(L))

def Nb0cc(X, L):
    if IsEmpty(L) == True:
        return 0
    else:
        if FirstElmt(L) == X:
            return Nb0cc(X, Tail(L)) + 1
        else:
            return Nb0cc(X, Tail(L))

def Vmax(L):
    return Nb0cc(max(L), L)
# APLIKASI
print(maxNb(L))


# 3
# DEFINISI DAN SPESIFIKASI
# LPrime(L) : list of integer --> list
#   {LPrime(L) menghasilkan list baru dari list L yang dimana isinya hanya bilangan prima}

# InsertAfter: list --> list
#   {InsertAfter(L,x,e) menghasilkan list baru dari list L dimana menambahkan elemen x setelah elemen e}
# REALISASI
def insertAfter(L, x, e):
    if IsEmpty(L) == True:
        return []
    else:
        if FirstElmt(L) == e:
            return [FirstElmt(L)] + [x] + insertAfter(Tail(L), x, e)
        else:
            return [FirstElmt(L)] + insertAfter(Tail(L), x, e)
        
def LPrime(L):
    if IsEmpty(L) == True:
        return []
    else:
        if IsPrime(FirstElmt(L)) == True:
            return Konso(FirstElmt(L), LPrime(Tail(L)))
        else:
            return LPrime(Tail(L))
# APLIKASI
print(insertAfter(L,2,"abs"))
print(LPrime(L))

# 5
# DEFINISI DAN SPESIFIKASI
# MakeMinus: 2 set --> set
#   {MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2}
# REALISASI
def MakeMinus(L1, L2):
    if IsEmpty(L1) == True:
        return []
    else:
        if IsMember(FirstElmt(L1), L2):
            return MakeMinus(Tail(L1), L2)
        else:
            return [FirstElmt(L1)] + MakeMinus(Tail(L1), L2)
# APLIKASI
print(MakeMinus(L1,L2))

# 6
# DEFINISI DAN SPESIFIKASI
# MakeKomplemen: 2 set --> set
#   {MakeKomplemen(H1,H2) membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2 
#    tetapi bukan interseksi keduanya}
# REALISASI
def ListCombine(L1, L2):
    return L1 + L2

def MakeKomplemen1(L):
    if IsEmpty(L) == True:
        return []
    else:
        if not(IsMember(FirstElmt(L), Tail(L))):
            return [FirstElmt(L)] + MakeKomplemen1(Tail(L))
        else:
            return MakeKomplemen1(Tail(L))

def MakeKomplemen(L1,L2):
    return MakeKomplemen1(ListCombine(L1,L2))
# APLIKASI
print(MakeKomplemen(L1,L2))
print(max(L))
print(MakeMinus(L1,L2))