# Nama file: wujud_air.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 20 September 2021
# Deskripsi: menyatakan wujud air melalui temperaturnya dalam derajat Celcius dan pada tekanan 1 atm

# Definisi dan Spesifikasi dari fungsi wujud_air.py yang bernama WujudAir(x) adalah:
# WujudAir : integer --> string
#   WujudAir(x) menyatakan wujud air melalui temperatur suhunya yang bernilai x

# Realisasi
def WujudAir(x):
    if x > 0:
        if x < 100:
            return "Cair"
        else:
            return "Gas (uap air)"
    else:
        return "Padat"

# Aplikasi
print(WujudAir(-7))
print(WujudAir(50))
print(WujudAir(111))