# Nama file: pecahan.py
# Deskripsi: membuat tipe bentukan Pecahan beserta konstruktor dan selektornya
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 27 September 2021

# DEFINISI TYPE
# type Pecahan : <n : integer >= 0, d : integer != 0>
#   {<n:integer >=0, d:integer >0>  n adalah pembilang (numerator) dan d adalah penyebut (denumerator). Penyebut sebuah Pecahan tidak boleh nol}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP : integer >=0, integer > 0 --> Pecahan
#   {MakeP(x,y) membentuk sebuah Pecahan dari pembilang x dan penyebut y, dengan x dan y integer}
# Realisasi dalam Python
class Pecahan:
    def __init__(self,x,y):
        self.n = x
        self.d = y

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Pemb : Pecahan --> integer >=0
#   {Pemb(p) memberikan numerator pembilang n dari pecahan tsb}
# Realisasi dalam Python
def Pemb(p):
    return p.n

# Peny : Pecahan --> integer > 0
#   {Peny(p) memberikan denumerator penyebut d dari Pecahan tsb}
# Realisasi dalam Python
def Peny(p):
    return p.d

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP : 2 Pecahan → boolean
#   {IsEqP(p1,p2) true jika p1 = p2
#   Membandingkan apakah dua buah Pecahan sama nilainya: n1/d1 = n2/d2 jika dan hanya jika n1d2 = n2d1}
# Realiasi dalam Python
def IsEqP(p1,p2):
    return (Pemb(p1)/Peny(p1)) == (Pemb(p2)/Peny(p2))

# IsLtP : 2 Pecahan → boolean
#  {IsLtP(p1,p2) true jika p1 < p2
#  Membandingkan dua buah Pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 < n2/d2 jika dan hanya jika n1d2 < n2d1}
# Realisasi dalam Python
def IsLtP(p1,p2):
    return (Pemb(p1)/Peny(p1)) < (Pemb(p2)/Peny(p2))

# IsGtP : 2 Pecahan → boolean
#  {IsGtP(p1,p2) true jika p1 > p2
# Membandingkan nilai dua buah Pecahan, apakah p1 lebih besar nilainya dari p2: n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1}
# Realisasi dalam Python
def IsGtP(p1,p2):
    return (Pemb(p1)/Peny(p1)) > (Pemb(p2)/Peny(p2))

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP PECAHAN
# AddP : 2 Pecahan → Pecahan
#  {AddP(P1,P2) : Menambahkan dua buah Pecahan P1 dan P2 :
#  n1/d1 + n2/d2 = (n1*d2 + n2*d1)/d1*d2 }
# Realisasi dalam Python
def AddP(P1,P2):
    return Pecahan(Pemb(P1)*Peny(P2) + Pemb(P2)*Peny(P1),Peny(P1)*Peny(P2))

# SubP : 2 Pecahan → Pecahan
#  {SubP(P1,P2) : Mengurangkan dua buah Pecahan P1 dan P2
#  Mengurangkan dua Pecahan : n1/d1 - n2/d2 = (n1*d2 - n2*d1)/d1*d2}
# Realisasi dalam Python
def SubP(P1,P2):
    return Pecahan(Pemb(P1)*Peny(P2) - Pemb(P2)*Peny(P1),Peny(P1)*Peny(P2))

# MulP : 2 Pecahan → Pecahan
#  {MulP(P1,P2) : Mengalikan dua buah Pecahan P1 dan P2
#  Mengalikan dua Pecahan : n1/d1 * n2/d2 = n1*n2/d1*d2}
# Realisasi dalam Python
def MulP(P1,P2):
    return Pecahan(Pemb(P1)*Pemb(P2),Peny(P1)*Peny(P2))

# DivP : 2 Pecahan → Pecahan
#  {DivP(P1,P2) : Membagi dua buah Pecahan P1 dan P2
#  Membagi dua Pecahan : (n1/d1)/(n2/d2) = n1*d2/d1*n2}
# Realisasi dalam Python
def DivP(P1,P2):
    return Pecahan(Pemb(P1)*Peny(P2),Peny(P1)*Pemb(P2))

# RealP : Pecahan → real
#  {Menuliskan bilangan Pecahan dalam notasi desimal }
# Realisasi dalam Python
def RealP(P):
    return Pemb(P)/Peny(P)

#Aplikasi
A = Pecahan(21,7)
B = Pecahan(3,2)
print(Pemb(A))
print(Peny(A))
print(IsEqP(A,Pecahan(6,5)))
print(IsLtP(A,B))
print(IsGtP(A,B))
print("{}/{}".format(Pemb(AddP(A,B)), Peny(AddP(A,B))))
print("{}/{}".format(Pemb(SubP(A,B)), Peny(SubP(A,B))))
print("{}/{}".format(Pemb(MulP(A,B)),Peny(MulP(A,B))))
print("{}/{}".format(Pemb(DivP(A,B)),Peny(DivP(A,B))))
print(RealP(DivP(A,B)))
print(RealP(A))