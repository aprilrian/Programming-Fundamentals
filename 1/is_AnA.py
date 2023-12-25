# Nama file: is_AnA.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 4 September 2021
# Deskripsi: menentukan nilai boolean suatu karakter yang bernilai benar/true jika karakter tersebut adalah huruf 'A', atau salah/false jika karakter tersebut adalah huruf selain 'A'

# Definisi dan spesifikasi dari fungsi is_AnA bernama is_AnA(x) adalah:
# is_AnA : character --> boolean
#   is_AnA(x) benar jika (x) adalah karakter (huruf) 'A', atau salah jika x adalah karakter (huruf) selain 'A'

# Realisasi

def is_AnA(x):
    return (x == 'A')

# Aplikasi
is_AnA(1)
is_AnA(0)
is_AnA(-1)
is_AnA('A')
is_AnA('X')
