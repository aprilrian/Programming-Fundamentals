# Nama file: is_positif.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 4 September 2021
# Deskripsi: menentukan nilai boolean suatu bilangan integer yang bernilai benar/true jika bilangan tersebut positif, atau salah/false jika bilangan tersebut negatif

# Definisi dan spesifikasi dari fungsi is_positif bernama is_positif(x) adalah:
# is_positif : integer --> boolean
#   is_positif(x) benar jika (x) positif, atau salah jika x negatif

# Realisasi

def is_positif(x):
    return (x >= 0)

# Aplikasi
is_positif(1)
is_positif(0)
is_positif(-1)
