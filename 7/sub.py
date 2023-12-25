# Nama file: sub.py
# Deskripsi: pengurangan 2 bilangan integer
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# sub : 2 integer >= 0 --> integer >= 0
#  {sub(x,y) mengurangkan x dan y}
#   sub (x,y) = x - y
#               = x - (1 - (y-1))

# REALISASI
def sub(x,y):
    if y == 0:
        return x
    else:
        return sub(x,y-1) - 1

# APLIKASI
print(sub(3,2))
print(sub(5,0))
print(sub(8,3))