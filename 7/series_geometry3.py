# Nama file: series_geometry3.py
# Deskripsi: menghitung deret geometri: 1 + 3 + 9 + 27 + ...
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# ser_ge3 : integer > 0 --> integer > 0
#  {ser_ge3(n) menghitung deret geometri: 1 + 3 + 9 + 27 + n}
#   ser_ge3(n) = ser_ge3(n-1) + pow(3,n-1)

# pow : 2 integer > 0 --> integer > 0
#  {pow(x,y) menghasilkan hasil perpangkatan x dengan y}
#   pow(x,y) = x ^ y
#            = x ** y
#            = mul(pow(x, y-1), x)

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

def pow(x,y):
    if y == 1:
        return x
    else:
        return mul(pow(x,y-1),x)
    
def ser_ge3(n):
    if n == 1:
        return 1
    else:
        return ser_ge3(n-1) + pow(3,n-1)
    
# APLIKASI
print(ser_ge3(5))
print(ser_ge3(3))
print(ser_ge3(7))