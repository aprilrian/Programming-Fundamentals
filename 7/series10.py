# Nama file: series10.py
# Deskripsi: menghitung deret: 1 + 4 + 16 + ...
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# ser10 : integer > 0 --> integer > 0
#  {ser10(n) menghitung deret: 1 + 4 + 16 + n}
#   ser10(n) = 

# mul : 2 integer > 0 --> integer > 0
#  {mul(x,y) mengalikan x dengan y}
#   mul(x,y) = x * y
#            = x + x + (y-1) 

# REALISASI
def mul(x,y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + mul(x,y-1)

def ser10(n):
    if n == 1:
        return 1
    else:
        return ser10(n-1) + mul(n, n)

# APLIKASI
print(ser10(4))
print(ser10(3))
print(ser10(10))