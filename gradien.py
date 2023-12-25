# Nama File : gradien.py
# Pembuat : Ardian Fajar Widyaputra, Aprilyanto Setiyawan Siburian
# Tanggal : 8 Oktober 2021
# Deskripsi : Membuat tipe data bentukan garis beserta konstruktor dan selektornya

# DEFINISI TIPE 1
# type point : <a:integer, b:integer>
#   {<a:integer, b:integer> adalah sebuah point, dengan a adalah absis
#   dan d adalah ordinat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR 1
# MakePoint : 2 integer --> point
#   {MakePoint(a,b) membentuk sebuah point dari a dan b dengan a sebagai 
#   absis dan b sebagai ordinat} 
# Realisasi dalam Python
def Point(a,b):
    return [a,b]

#  DEFINISI DAN SPESIFIKASI SELECTOR 1
# Absis : point --> integer
#   {Absis(P) memberikan Absis point P}
# Realisasi dalam Python
def Absis(P):
    return P[0]

# Ordinat : point --> integer
#   {Ordinat(P) memberikan Ordinat point P}
# Realisasi dalam Python
def Ordinat(P):
    return P[1]

# DEFINISI TIPE 2
# type Garis : <P1:point, P2:point>
#   {<P1:point, P2:point> adalah sebuah garis, yang dimana P1 adalah point 1 dan P2 adalah point 2}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR 2
# MakeGaris : 2 point --> Garis
#   {MakeGaris(P1,P2) membentuk sebuah garis dari P1 dan P2, dengan P1 sebagai point 1 dan P2 sebagai point 2} 
# Realisasi dalam Python
def Garis(P1,P2):
    return [P1,P2]

# DEFINISI DAN SPESIFIKASI SELEKTOR 2
# point1 : Garis --> integer
#   {point1(P) memberikan point pertama ke garis P}
# Realisasi dalam Python
def point1(P):
    return P[0]

# point2 : PointC --> integer
#   {point2(P) memberikan point kedua ke garis P}
# Realisasi dalam Python
def point2(P):
    return P[1]

# DEFINISI DAN SPESIFIKASI OPERATOR
# Gradien : Garis --> real
#   {Gradien(P) menghitung gradien garis P}
# Realisasi dalam Python
def Gradien(P):
    return (Ordinat(point2(P))-Ordinat(point1(P)))/(Absis(point2(P))-Absis(point1(P)))

# PanjangGaris : Garis --> real
#   {PanjangGaris(P) menghitung panjang garis P}
# Realisasi dalam Python
from math import sqrt
def PanjangGaris(P):
    return sqrt((abs(Absis(point1(P))-Absis(point2(P))))**2 + (abs(Ordinat(point1(P))-Ordinat(point2(P))))**2)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSejajar : 2 Garis --> Boolean
#   {IsSejajar(P1,P2) membandingkan 2 buah garis, akan TRUE jika gradien garis 1 sama dengan gradien garis 2}
# Realisasi dalam Python
def IsSejajar(P1,P2):
    if Gradien(P1)==Gradien(P2):
        return True
    else:
        return False

# IsTegakLurus : 2 Garis --> Boolean
#   {IsTegakLurus(P1,P2) membandingkan 2 buah garis, akan TRUE jika gradien garis 1 dikali gradien garis 2 sama dengan -1}
# Realisasi dalam Python
def IsTegakLurus(P1,P2):
    if Gradien(P1)*Gradien(P2)==-1:
        return True
    else:
        return False

# APLIKASI
P1 = ((2,4),(3,6))
P2 = ((4,8),(6,12))
print(point1(P1))
print(point2(P1))
print(Gradien(P1))
print(PanjangGaris(P1))
print(IsSejajar(P1,P2))
print(IsTegakLurus(P1,P2))
