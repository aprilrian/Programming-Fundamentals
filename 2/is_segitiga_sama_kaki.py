# Nama file: is_segitiga_sama_kaki.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 10 September 2021
# Deskripsi: mengecek apakah 3 nilai panjang sisi segitiga membentuk segitiga sama kaki

# Definisi dan spesifikasi dari fungsi is_segitiga_sama_kaki yang bernama IsSegitigaSamaKaki(a,b,c) adalah:
# IsSegitigaSamaKaki : 3 integer > 0 --> boolean
#   IsSegitigaSamaKaki(a,b,c) bernilai True apabila memenuhi salah satu ciri segitiga sama kaki berikut, yaitu jika a = b maka a, b ≠ c; jika b = c maka b, c ≠ a; jika a = c maka a, c ≠ b

# Realisasi
def IsSegitigaSamaKaki(a,b,c):
    if ((a > 0) and (b > 0) and (c > 0)):
        return ((a == b and a != c and b != c) or (b == c and b != a and c != a) or (a == c and a != b and c != b))

    else:
        return 'Masukan tidak valid.'

# Aplikasi
print(IsSegitigaSamaKaki(2,2,2))
print(IsSegitigaSamaKaki(3,5,5))
print(IsSegitigaSamaKaki(7,8,11))
print(IsSegitigaSamaKaki(-3,2,-4))