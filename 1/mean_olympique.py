# Nama file: mean_olympique.py
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 4 September 2021
# Deskripsi: menghitung nilai rata-rata dari 2 bilangan integer, yang bukan maksimum dan bukan minimum dari 4 bilangan integer

# Definisi dan spesifikasi dari fungsi mean_olympique bernama MO(a,b,c,d) adalah:
# MO : 4 integer ≥ 0 --> real
#   MO(a,b,c,d) menghitung nilai rata-rata dari 2 bilangan integer, yang bukan maksimum dan bukan minimum dari 4 bilangan integer a, b, c dan d

# min4 : 4 integer > 0 --> integer
#   min4(a,b,c,d) menentukan nilai minimum dari 4 bilangan integer a, b, c dan d

# max4 : 4 integer > 0 --> integer
#   max4(a,b,c,d) menentukan nilai maksimum dari 4 bilangan integer a, b, c dan d

# min2 : 2 integer > 0 --> integer
#   min2(x,y) menentukan nilai minimum dari 2 bilangan integer x dan y, hanya dengan ekspresi aritmatika: jumlah dari kedua bilangan - selisih kedua bilangan, hasilnya dibagi 2

# max2 : 2 integer > 0 --> integer
#   max2(x,y) menentukan nilai maksimum dari 2 bilangan integer x dan y, hanya dengan ekspresi aritmatika: jumlah dari kedua bilangan + selisih kedua bilangan, hasilnya dibagi 2

# Realisasi
def max2(x,y):
    return((x+y) + abs(x-y)) // 2

def min2(x,y):
    return((x+y) - abs(x-y)) // 2

def max4(a,b,c,d):
    return max2(max2(a,b),max2(c,d))

def min4(a,b,c,d):
    return min2(min2(a,b),min2(c,d))

def MO(a,b,c,d):
    return (a+b+c+d-min4(a,b,c,d) - max4(a,b,c,d)) // 2

# Aplikasi
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
print(MO(8,12,10,20))
