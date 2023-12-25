# Nama file: series_arithmetic3.py
# Deskripsi: menghitung deret aritmatika: 3 + 6 + 9 + ...
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# mul3 : integer > 0 --> integer > 0
#  {mul3(n) menghitung hasil perkalian n dengan 3}
#   mul3(n) = 3 * n
#           = 3 + mul3(n-1)

# ser_ar3 : integer > 0 --> integer > 0
#  {ser_ar3(n) menghitung deret aritmatika: 3 + 6 + 9 + ... sejauh n atau n sebagai suku deret terakhir}
#   ser_ar3(n) = ser_ar3(n-1) + mul3(n)

# REALISASI
def mul3(n):
    if n == 1:
        return 3
    else:
        return 3 + mul3(n-1)

def ser_ar3(n):
    if n == 1:
        return 3
    else:
        return ser_ar3(n-1) + mul3(n)

# APLIKASI
print(ser_ar3(3))
print(ser_ar3(5))
print(ser_ar3(7))