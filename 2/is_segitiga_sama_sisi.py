# Nama file: is_segitiga_sama_sisi.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 10 September 2021
# Deskripsi: mengecek apakah 3 nilai panjang sisi segitiga membentuk segitiga sama sisi

# Definisi dan spesifikasi dari fungsi is_segitiga_sama_sisi yang bernama IsSegitigaSamaSisi(a,b,c) adalah:
# IsSegitigaSamaSisi : 3 integer > 0 --> boolean
#   IsSegitigaSamaSisi(a,b,c) bernilai True apabila tiga integer a,b dan c bernilai sama yang merupakan salah satu ciri segitiga sama sisi

# Realisasi
def IsSegitigaSamaSisi(a,b,c):
    if ((a > 0) and (b > 0) and (c > 0)):
        return (a == b == c)
        
    else:
        return 'Masukan tidak valid.'

# Aplikasi
print(IsSegitigaSamaSisi(2,2,2))
print(IsSegitigaSamaSisi(3,5,5))
print(IsSegitigaSamaSisi(7,8,11))
print(IsSegitigaSamaSisi(-3,2,-4))