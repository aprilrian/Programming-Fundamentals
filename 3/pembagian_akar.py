# Nama file: pembagian_akar.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 20 September 2021
# Deskripsi : menghitung hasil bagi akar-akar persamaan kuadrat menggunakan rumus abc dengan masukan 3 integer

# Definisi dan Spesifikasi dari fungsi pembagian_akar.py yang bernama PembagianAkar(x,y,z) adalah:
# PembagianAkar : 3 integer --> real
#   PembagianAkar(x,y,z) menghitung hasil bagi akar positif dan negatif dari suatu persamaan kuadrat melalui 3 integer a,b,c sebagai koefisien

# akar_positif : 3 integer --> real
#   akar_positif(a,b,c) menyatakan hasil perhitungan rumus abc positif dari suatu persamaan kuadrat melalui 3 integer x,y,z sebagai koefisiennya

# akar_negatif : 3 integer --> real
#   akar_negatif(a,b,c) menyatakan hasil perhitungan rumus abc negatif dari suatu persamaan kuadrat melalui 3 integer x,y,z sebagai koefisiennya

# Realisasi
def akar_positif(a,b,c):
    return (b*(-1) + (b**2-4*a*c)**0.5)/(2*a)

def akar_negatif(a,b,c):
    return (b*(-1) - (b**2-4*a*c)**0.5)/(2*a)

def PembagianAkar(x,y,z):
    if akar_positif(x,y,z) > akar_negatif(x,y,z):
        return akar_positif(x,y,z) / akar_negatif(x,y,z)
    else:
        return akar_negatif(x,y,z) / akar_negatif(x,y,z)

# Aplikasi
print(PembagianAkar(1,4,3))
print(PembagianAkar(1,-6,8))




