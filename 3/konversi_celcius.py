# Nama file: konversi_celcius.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 20 September 2021
# Deskripsi: mengonversi besaran derajat suhu dalam Celcius ke Reamur, Fahrenheit atau Kelvin sesuai dengan kode konversi

# Definisi dan Spesifikasi dari fungsi konversi_celcius.py yang bernama KonversiCelcius(a,b) adalah:
# KonversiCelcius : integer, string --> real
#   KonversiCelcius(a,b) mengonversi nilai derajat Celcius a ke nilai derajat sesuai kode konversi b

# Realisasi
def KonversiCelcius(a,b):
    if b == "reamur":
        return 4*a/5
    elif b == "fahrenheit":
        return (9*a/5) + 32
    elif b == 'kelvin':
        return a + 273.15
    else:
        return "Masukan tidak valid."

# Aplikasi
print(KonversiCelcius(11,'reamur'))
print(KonversiCelcius(32,'kilometer'))
print(KonversiCelcius(2,'kelvin'))