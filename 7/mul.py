# Nama file: mul.py
# Deskripsi: perkalian 2 bilangan integer
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
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

# APLIKASI
print(mul(2,4))
print(mul(5,3))
print(mul(7,0))