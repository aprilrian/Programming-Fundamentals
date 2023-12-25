# Nama File : hargabersih.py
# Nama Pembuat : Aprilyanto Setiyawan Siburian
# Tanggal : 10 Oktober 2021
# Deskripsi : Mengembalikan harga bersih produk setelah dipotong diskon

# DEFINISI DAN SPESIFIKASI
# premium : string --> string
#   {premium(x) memberikan kategori premium ke pelanggan}

# gold : string --> string
#   {gold(x) memberikan kategori gold ke pelanggan}

# silver : string --> string
#   {silver(x) memberikan kategori silver ke pelanggan}

# hargabersih : integer, string --> real
#   {hargabersih(harga, kategori) mengembalikan harga bersih produk dari harga setelah dipotong diskon sesuai 
# aturan dan kategori}

# REALISASI
def premium(x):
    return "Anggota Premium"

def gold(x):
    return "Anggota Gold"

def silver(x):
    return "Anggota Silver"
    
def hargabersih(harga, kategori):
    if harga > 1000000 and kategori == premium:
        return f'Rp.{harga - harga * 0.35}, {kategori(premium)}'
    elif 750000 < harga <= 1000000 and kategori == premium:
        return f'Rp.{harga - harga * 0.25}, {kategori(premium)}'
    elif 500000 < harga <= 750000 and kategori == premium:
        return f'Rp.{harga - harga * 0.15}, {kategori(premium)}'
    elif harga < 5000000 and kategori == premium:
        return f'Rp.{harga - harga * 0.10}, {kategori(premium)}'
    elif harga > 1000000 and kategori == gold:
        return f'Rp.{harga - harga * 0.325}, {kategori(gold)}'
    elif 750000 < harga <= 1000000 and kategori == gold:
        return f'Rp.{harga - harga * 0.225}, {kategori(gold)}'
    elif 500000 < harga <= 750000 and kategori == gold:
        return f'Rp.{harga - harga * 0.125}, {kategori(gold)}'
    elif harga < 5000000 and kategori == gold:
        return f'Rp.{harga - harga * 0.075}, {kategori(gold)}'
    elif harga > 1000000 and kategori == silver:
        return f'Rp.{harga}, {kategori(silver)}'
    elif 750000 < harga <= 1000000:
        return f'Rp.{harga}, {kategori(silver)}'
    elif 500000 < harga <= 750000:
        return f'Rp.{harga}, {kategori(silver)}'
    elif harga < 500000 and kategori == silver:
        return f'Rp.{harga}, {kategori(silver)}'
    else:
        return f'Tidak ada Transaksi.'
      
# APLIKASI
print(f'------------PREMIUM------------')
print(hargabersih(700000, premium))
print(hargabersih(1200000, premium))
print(hargabersih(3300000, premium))
print(hargabersih(1100000, premium))
print(f'-------------GOLD------------')
print(hargabersih(4400000, gold))
print(hargabersih(500000, gold))
print(hargabersih(1000000, gold))
print(hargabersih(1100000, gold))
print(f'------------SILVER------------')
print(hargabersih(400000, silver))
print(hargabersih(200000, silver))
print(hargabersih(1100000, silver))
print(hargabersih(1300000, silver))