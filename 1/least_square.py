# Nama file: least_square.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 4 September 2021
# Deskripsi: menghitung jarak dua buah titik atau panjang garis yang dibentuk oleh dua buah titik, yang terdiri dari 4 bilangan riil

# Definisi dan spesifikasi dari fungsi least_square bernama LS(x1,x2,y1,y2) adalah:
# LS : 4 real --> real
#   LS(x1,x2,y1,y2) menghitung jarak antara 2 buah titik (x1,x2) dengan (y1,y2)

# dif2 : 2 real --> real
#   dif2(x,y) menghitung nilai kuadrat dari selisih (x,y)

# FX2 : real --> real
#   FX2(x) menghitung nilai kuadrat dari (x)

# Realisasi
def FX2(x):
    return x*x

def dif2(x,y):
    return FX2(x-y)

def LS(x1,y1,x2,y2):
    return ((dif2(y2,y1)) + (dif2(x2,x1))) ** 0.5

# Aplikasi
LS(1,3,5,6)
LS(2,5,7,10)
LS(92,5,31,4)
