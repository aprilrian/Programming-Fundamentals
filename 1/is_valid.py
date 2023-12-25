# Nama file: is_valid.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 4 September 2021
# Deskripsi: menentukan validitas suatu bilangan integer melalui nilai boolean yang bernilai benar/true jika bilangan tersebut nilainya lebih kecil dari 5 atau lebih besar dari 500

# Definisi dan spesifikasi dari fungsi is_valid bernama is_valid(x) adalah:
# is_valid : integer --> boolean
#   is_valid(x) benar jika (x) bernilai lebih kecil dari 5 atau lebih besar dari 500

# Realisasi

def is_valid(x):
    return (x < 5) or (x > 500)

# Aplikasi
is_valid(5)
is_valid(0)
is_valid(500)
is_valid(6000)
