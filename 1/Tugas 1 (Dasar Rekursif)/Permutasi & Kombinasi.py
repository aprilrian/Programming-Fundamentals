# Nama file     : Permutasi & Kombinasi.py
# Pembuat       : Aprilyanto Setiyawan Siburian
# Tanggal       : 23 Oktober 2021
# Deskripsi     : Menghitung permutasi dan kombinasi dengan menggunakan fungsi faktorial rekursif
               
              
# DEFINISI DAN SPESIFIKASI 
# faktorial_rekursif : integer > 0 --> integer > 0
#   {faktorial_rekursif(n) = n! sesuai dengan definisi rekursif faktorial}

# Permutasi : 2 integer >= 0 --> integer > 0
#   {Permutasi(n,r) menghitung susunan suatu kumpulan objek dalam urutan yang berbeda dari urutan yang semula dengan memperhatikan urutan, 
#   n sebagai jumlah kumpulan objek dan r sebagai jumlah objek yang akan dipilih}

# Kombinasi : 2 integer >= 0 --> integer > 0
#   {Kombinasi(n,r) menghitung susunan suatu kumpulan objek dalam urutan yang berbeda dari urutan yang semula tanpa memperhatikan urutan, 
#   n sebagai jumlah kumpulan objek dan r sebagai jumlah objek yang akan dipilih}

# REALISASI
def faktorial_rekursif(n):
    if n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n-1)

def Permutasi(n,r):
    if n > r:
        return faktorial_rekursif(n) // faktorial_rekursif(n-r)
    else:
        return "Masukan tidak valid."
    
def Kombinasi(n,r):
    if n > r:
        return faktorial_rekursif(n) // (faktorial_rekursif(r) * faktorial_rekursif(n-r))
    else:
        return "Masukan tidak valid."


# APLIKASI
print(Permutasi(2,1))
print(Permutasi(11,3))
print(Permutasi(11,31))
print(Kombinasi(7,2))
print(Kombinasi(11,3))
print(Kombinasi(12,4))
