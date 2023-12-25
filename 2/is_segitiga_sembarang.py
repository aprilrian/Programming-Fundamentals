# Nama file: is_segitiga_sembarang.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 10 September 2021
# Deskripsi: mengecek apakah 3 nilai panjang sisi segitiga membentuk segitiga sembarang

# Definisi dan spesifikasi dari fungsi is_segitiga_sembarang yang bernama IsSegitigaSembarang(a,b,c) adalah:
# IsSegitigaSembarang : 3 integer > 0 --> boolean
#   IsSegitigaSembarang(a,b,c) bernilai True jika ketiga integer bernilai beda dan memenuhi salah satu ciri segitiga sembarang berikut, yaitu a + b > c, b + c > a, a + c > b

# Realisasi
def IsSegitigaSembarang(a,b,c):
    if ((a > 0) and (b > 0) and (c > 0)):
        return ((a != b != c) and (a + b > c and b + c > a and a + c > b))

    else:
        return 'Masukan tidak valid.'

# Aplikasi
print(IsSegitigaSembarang(2,2,2))
print(IsSegitigaSembarang(3,5,5))
print(IsSegitigaSembarang(7,8,11))
print(IsSegitigaSembarang(-3,2,-4))