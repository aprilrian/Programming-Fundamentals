# Nama file: series_integer.py
# Deskripsi: menghitung deret bilangan integer
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# ser_int : integer > 0 --> integer > 0
#  {ser_int(n) menghitung deret bilangan integer sejauh n atau dengan n sebagai suku deret terakhir}
#   ser_int(n) = n + ser_int(n-1)

# REALISASI
def ser_int(n):
    if n == 1:
        return 1
    else:
        return n + ser_int(n-1)

# APLIKASI
print(ser_int(5))
print(ser_int(10))
print(ser_int(4))