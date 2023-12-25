# Nama file: mul3.py
# Deskripsi: menghitung perkalian input dengan 3
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# mul3 : integer > 0 --> integer > 0
#  {mul3(n) menghitung hasil perkalian n dengan 3}
#   mul3(n) = 3 * n
#           = 3 + mul3(n-1)

# REALISASI
def mul3(n):
    if n == 1:
        return 3
    else:
        return 3 + mul3(n-1)

# APLIKASI
print(mul3(3))
print(mul3(5))
print(mul3(9))