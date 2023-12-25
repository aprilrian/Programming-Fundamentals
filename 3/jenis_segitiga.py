# Nama file: jenis_segitiga.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 20 September 2021
# Deskripsi: menyatakan jenis segitiga melalui nilai masukan 3 integer sebagai panjang setiap sisinya

# Definisi dan Spesifikasi dari fungsi jenis_segitiga.py yang bernama JenisSegitiga(a,b,c) adalah:
# JenisSegitiga : 3 integer > 0 --> string
#   JenisSegitiga(a,b,c) menyatakan jenis segitiga melalui nilai masukan 3 integer a,b,c sebagai panjang setiap sisinya

# Realisasi
def JenisSegitiga(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a == b and b == c:
            return "Segitiga sama sisi"
        elif (a == b and a != c and b != c) or (b == c and b != a and c != a) or (a == c and a != b and c != b):
            return  "Segitiga sama kaki"
        else:
            return "Segitiga sembarang"
    else:
        return "Masukan tidak valid."

# Aplikasi        
print(JenisSegitiga(2,4,3))
print(JenisSegitiga(3,3,3))
print(JenisSegitiga(2,4,4))