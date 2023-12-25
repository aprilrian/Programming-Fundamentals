# Nama file: pow.py
# Deskripsi: perpangkatan bilangan integer
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# mul : 2 integer > 0 --> integer > 0
#  {mul(x,y) mengalikan x dengan y}
#   mul(x,y) = x * y
#            = x + x + (y-1)

# pow : 2 integer > 0 --> integer > 0
#  {pow(x,y) menghasilkan hasil perpangkatan x dengan y}
#   pow(x,y) = x ^ y
#            = x ** y
#            = mul(pow(x, y-1), x)

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

# APLIKASI
print(pow(3,4))
print(pow(5,5))
print(pow(2,2))