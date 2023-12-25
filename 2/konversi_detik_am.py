# Nama file: konversi_detik_am.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 10 September 2021
# Deskripsi: menghitung detik dari jam tertentu terhitung mulai jam 00:00:00 am tanggal yang bersangkutan

# Definisi dan spesifikasi dari fungsi konversi_detik_am bernama KonversiDetikAM(j,m,s,k) adalah:
# KonversiDetikAM : 3 integer ≥ 0, 1 string --> integer
#   KonversiDetikAM(j,m,s,k) menghitung jumlah detik dari hasil konversi j jam, m menit dan menjumlahkannya dengan s detik serta k yang menyatakan 'Am' atau 'Pm' pada jam tersebut

# Realisasi
def KonversiDetikAM(j,m,s,k):
    if ((j >= 0) and (m >= 0) and (s >= 0)):
    
        if (k == ("am") or ("AM") or ("Am")):
            return ((j * 3600) + (m * 60) + s)

        elif ((k == 'pm') or (k == 'PM') or (k == 'Pm')):
            return (((j + 12) * 3600) + (m * 60) + s)

        else:
            return 'Masukan tidak valid.'

    else:
        return 'Masukan tidak valid.'

# Aplikasi
print(KonversiDetikAM(1,2,1,'pm'))
print(KonversiDetikAM(1,1,0,'AM'))
print(KonversiDetikAM(1,1,1,'aw'))
print(KonversiDetikAM(-1,1,1,'am'))