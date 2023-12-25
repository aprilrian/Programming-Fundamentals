# Nama file: konversi_detik.py
# Pembuat: Aprilyanto Setiyawan Siburian   
# Tanggal: 10 September 2021
# Deskripsi: menghitung detik dari jam tertentu terhitung mulai jam 00:00:00 tanggal yang bersangkutan

# Definisi dan spesifikasi dari fungsi konversi_detik bernama KonversiDetik(j,m,s) adalah:
# KonversiDetik : 3 integer ≥ 0 --> integer
#   KonversiDetik(j,m,s) menghitung jumlah detik dari hasil konversi j jam dan m menit serta menjumlahkannya dengan s detik

# Realisasi
def KonversiDetik(j,m,s):
    if ((j >= 0) and (m >= 0) and (s >= 0)):
        return ((j * 3600) + (m * 60) + s)
    
    else:
        return ('Masukan tidak valid')

# Aplikasi
print(KonversiDetik(11,3,4))
print(KonversiDetik(10,1,55))
print(KonversiDetik(-1,-9,11))