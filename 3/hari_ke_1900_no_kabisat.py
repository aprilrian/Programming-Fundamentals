# Nama file: hari_ke_1900_no_kabisat.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 20 September 2021
# Deskripsi: menghitung jumlah hari dari tanggal yang dimasukkan mulai 1 Januari tanpa memperhitungkan tahun kabisat

# Definisi dan spesifikasi dari fungsi hari_ke_1900_no_kabisat.py yang bernama HariKe1900NoKabisat(d,m,y) adalah:
# HariKe1900NoKabisat : 1 <= integer <= 31, 1 <= integer <= 12, 0 <= integer <= 99 --> 1 <= integer <= 366
#   HariKe1900NoKabisat(d,m,y) dari suatu tanggal (d,m,y) adalah hari 'absolut' dihitung mulai 1 Januari + y tanpa memperhitungkan tahun kabisat

# dpm : 1 <= integer <= 12 --> 1 <= integer <= 36
#   dpm(B) adalah jumlah kumulatif hari pada tahun yang bersangkutan dari tanggal 1 Januari sampai dengan tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat

# Realisasi
def dpm(B):
    if B == 1 :
        return 1
    elif B == 2:
        return 32
    elif B == 3:
        return 60
    elif B == 4:
        return 91
    elif B == 5:
        return 121
    elif B == 6:
        return 152
    elif B == 7:
        return 182
    elif B == 8:
        return 213
    elif B == 9:
        return 244
    elif B == 10:
        return 274
    elif B == 11:
        return 305
    elif B == 12:
        return 335
    else:
        return "Tanggal tidak valid."

def HariKe1900NoKabisat(d,m,y):
    return dpm(m) + d - 1

# Aplikasi
print(HariKe1900NoKabisat(12,12,72))
print(HariKe1900NoKabisat(2,3,12))