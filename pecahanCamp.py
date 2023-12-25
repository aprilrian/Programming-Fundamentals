# Nama File : pecahanCamp.py
# Pembuat : Ardian Fajar Widyaputra , Aprilyanto Setiyawan Siburian
# Tanggal : 08 Oktober 2021
# Deskripsi : Membuat tipe data bentukan pecahan campuran beserta konstruktor dan selektornya

# -------------------------------------------------------------------------

# DEFINISI TIPE 

# type PecahanC : <bil:integer, n:integer>=0, d:integer>0>
#   {<bil:integer, n:integer>=0, d:integer>0> adalah sebuah pecahan, dengan bil adalah bilangan bulat pecahan campuran, 
#   n adalah pembilang pecahan campuran ,dan d adalah penyebut pecahan campuran. penyebut tidak boleh nol dan pembilang selalu harus lebih kecil dari penyebut.}

# -------------------------------------------------------------------------

# type Pecahan: <n:integer>=0, d:integer>0>
#   {<n:integer>=0, d:integer>0> adalah sebuah pecahan, dengan pemb adalah pembilang (numerator) 
#   dan peny adalah penyebut (denumerator)}

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakePecahanC : 3 integer --> PecahanC
#   {MakePecahanC(bil,n,d) membentuk sebuah pecahan campuran dari bil, n, dan d, dengan bil sebagai 
#   bilangan bulat pecahan campuran, n sebagai pembilang (numerator), dan d sebagai penyebut (denumerator)}

# MakePecahan : 2 integer --> pecahan
#   {MakePecahan(pemb, peny) membentuk sebuah pecahan dari pembilang dan penyebut dengan pemb sebagai 
#   pembilang dan penye sebagai penyebut}
#Realisasi
def PecahanC(bil,n,d):
    return [bil,n,d]

def Pecahan(a,b):
    return [a,b]

# -------------------------------------------------------------------------

#DEFINISI DAN SPESIFIKASI SELEKTOR
#bil : pecahan --> integer 
#{bil(pc) memberikan bilangan bulat dari pecahan campuran Pc}
#Realisasi
def bil(pc):
    return pc[0]

#n : pecahan --> integer 
#{n(pc) memberikan numerator pembilang bil dari pecahan campuran Pc}
#Realisasi
def n(pc):
    return pc[1]

#d : pecahan --> integer 
#{d(pc) memberikan denominator penyebut n dari pecahan campuran Pc}
#Realisasi
def d(pc):
    return pc[2]

#pembilang : pecahan --> integer 
#pembilang(pc) memberikan numerator pembilang n dari pecahan Pc}
#Realisasi
def pemb(pc):
    return pc[0]

#penyebut : pecahan --> integer 
#penyebut(pc) memberikan denominator penyebut n dari pecahan Pc}
#Realisasi
def peny(pc):
    return pc[1]

#KonversiPecahan : pecahan --> pecahan
#KonversiPecahan(P) mengubah pecahan campuran P ke tipe pecahan biasa (seperti 
#contoh yang ada di diktat, jika pecahan bernilai negatif, nilai negatif dilekatkan pada 
#pembilang)}
#Realisasi
def KonversiPecahan(P):
    if bil(pc) >= 0:
        return (bil(pc)*d(pc)+n(pc)),d(pc)
    else:
        return (bil(pc)*d(pc)-n(pc)),d(pc)

#KonversiR : pecahan --> pecahan
#KonversiPecahan(P) merubah dari pecahan menjadi bilangan real}
#Realisasi
def KonversiReal(P):
    if bil(pc) >= 0:
        return (bil(pc) * d(pc) + n(pc)) / d(pc)
    else:
        return (bil(pc) * d(pc) - n(pc)) / d(pc)

#KonversiPecahanCampuran : pecahan --> pecahan
#KonversiPecahanCampuran(pc) merubah dari pecahan biasa menjadi pecahan campuran}
#Realisasi
def KonversiPecahanCampuran(pc):
    return PecahanC(pemb(pc) // peny(pc), pemb(pc) % peny(pc), peny(pc))

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

#DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP PECAHAN
#AddP : 2 pecahanC → pecahan
#  { AddP(pc1,pc2) : Menambahkan dua buah pecahan P1 dan P2 :
#Realisasi
def AddP(pc1,pc2):
    return Pecahan((pemb(pc1) * peny(pc2) + pemb(pc2) * peny(pc1)), peny(pc1) * peny(pc2))
#AddPc : 2 pecahanC → pecahan
#  { AddPc(pc1,pc2) : Menambahkan dua buah pecahan campuran P1 dan P2 :
#Realisasi
def AddPc(pc1,pc2):
    return KonversiPecahanCampuran(AddP(KonversiPecahan(pc1),KonversiPecahan(pc2)))
#SubP : 2 pecahanC → pecahan
#  { SubP(pc1,pc2) : Mengurangkan dua buah pecahan P1 dan P2
#Realisasi
def SubP(pc1,pc2):
    return Pecahan((pemb(pc1) * peny(pc2) - pemb(pc2) * peny(pc1)), peny(pc1) * peny(pc2))
#SubPc : 2 pecahanC → pecahan
#  { SubPc(P1,P2) : Mengurangkan dua buah pecahan P1 dan P2
#Realisasi
def SubPc(pc1,pc2):
    return KonversiPecahanCampuran(SubP(KonversiPecahan(pc1),KonversiPecahan(pc2)))
#DivP : 2 pecahanC → pecahan
#  { DivP(pc1,pc2) : Membagi dua buah pecahan P1 dan P2
#Realisasi
def DivP(pc1,pc2):
    return Pecahan(pemb(pc1) * peny(pc2),peny(pc1) * pemb(pc2))
#DivPc : 2 pecahanC → pecahan
#  { DivPc(pc1,pc2) : Membagi dua buah pecahan P1 dan P2
#Realisasi
def DivPc(pc1,pc2):
    return KonversiPecahanCampuran(DivP(KonversiPecahan(pc1),KonversiPecahan(pc2)))
#MulP : 2 PecahanC --> pecahan
#   {MulP(P1,P2) mengalikan pecahan campuran P1 dan P2}
#Realisasi 
def MulP(pc1,pc2):
    return Pecahan(pemb(pc1) * pemb(pc2),peny(pc1) * peny(pc2))
#MulP : 2 PecahanC --> pecahan
#   {MulP(P1,P2) mengalikan pecahan campuran P1 dan P2}
#Realisasi 
def MulPc(pc1,pc2):
    return KonversiPecahanCampuran(MulP(KonversiPecahan(pc1),KonversiPecahan(pc2)))

# -------------------------------------------------------------------------

#DEFINISI DAN SPESIFIKASI PREDIKAT

#IsEqP? : 2 PecahanC --> Boolean
#   {IsEqP?(P1,P2) membandingkan apakah pecahan P1 sama dengan P2}
#Realisasi 
def IsEqP(pc1,pc2):
    return pemb(pc1) * peny(pc2) == peny(pc1) * pemb(pc2)
#IsEqP? : 2 PecahanC --> Boolean
#   {IsEqP?(P1,P2) membandingkan apakah pecahan P1 sama dengan P2}
#Realisasi 
def IsEqPc(pc1,pc2):
    return IsEqP(KonversiPecahan(pc1),KonversiPecahan(pc2))
# IsLtP? : 2 PecahanC --> Boolean
#   {IsLtP?(P1,P2) membandingkan apakah pecahan P1 lebih kecil dari P2}
# Realisasi 
def IsLtP(pc1,pc2):
    return pemb(pc1) * peny(pc2) < peny(pc1) * pemb(pc2)
# IsLtP? : 2 PecahanC --> Boolean
#   {IsLtP?(P1,P2) membandingkan apakah pecahan P1 lebih kecil dari P2}
# Realisasi 
def IsLtPc(pc1,pc2):
    return IsLtP(KonversiPecahan(pc1),KonversiPecahan(pc2))
# IsGtP? : 2 PecahanC --> Boolean
#   {IsGtP?(P1,P2) membandingkan apakah pecahan P1 lebih besar dari P2}
# Realisasi dalam Python
def IsGtP(pc1,pc2):
    return pemb(pc1) * peny(pc2) > peny(pc1) * pemb(pc2)
# IsGtP? : 2 PecahanC --> Boolean
#   {IsGtP?(P1,P2) membandingkan apakah pecahan P1 lebih besar dari P2}
# Realisasi dalam Python
def IsGtPc(pc1,pc2):
    return IsGtP(KonversiPecahan(pc1),KonversiPecahan(pc2))

# -------------------------------------------------------------------------# 
# -------------------------------------------------------------------------

#APLIKASI
pc = PecahanC(2,1,2)
print(bil(pc))
print(n(pc))
print(d(pc))
print(KonversiPecahan(pc))
print(KonversiReal(pc))
print(AddPc(PecahanC(2,1,2),(PecahanC(3,4,8))))
print(SubPc(PecahanC(2,1,2),(PecahanC(3,4,8))))
print(DivPc(PecahanC(2,1,2),(PecahanC(3,4,8))))
print(MulPc(PecahanC(2,1,2),(PecahanC(3,4,8))))
print(IsEqPc(PecahanC(2,1,2),(PecahanC(3,4,8))))
print(IsLtPc(PecahanC(2,1,2),(PecahanC(3,4,8))))
print(IsGtPc(PecahanC(2,1,2),(PecahanC(3,4,8))))