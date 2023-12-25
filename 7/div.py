# Nama file: div.py
# Deskripsi: pembagian 2 bilangan integer
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 24 Oktober 2021

# DEFINISI DAN SPESIFIKASI
# div : 2 integer > 0 --> integer > 0
#   {div(x,y) membagi x dengan y menghasilkan bilangan integer}
#    div(x,y) = x // y
#             = 1 + div(x-y,y)

# REALISASI
def div(x,y):
    if x < y:
        return 0
    else:
        return 1 + div(x-y,y)

# APLIKASI
print(div(3,2))
print(div(16,4))
print(div(22,3))