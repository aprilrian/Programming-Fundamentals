# Nama file: time.py
# Nama Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 10 Oktober 2021
# Deskripsi: Untuk mengembalikan sebuah time baru setelah n detik dari sebuah time

# DEFINISI DAN SPESIFIKASI TYPE
# type Time : <j:integer [0..24], m:integer [0..59], d:integer [0..59]> 
#   {<j:integer [0..24], m:integer [0..59], d:integer [0..59]> adalah sebuah tipe time yang terdiri dari j jam, m menit, dan d detik}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# j : Time --> integer [0..24]
#   {j(T) memberikan nilai j yang menyatakan satuan jam ke type T}

# m : Time --> integer [0..59]
#   {m(T) memberikan nilai m yang menyatakan satuan menit ke type T}

# d : Time --> integer [0..59]
#   {d(T) memberikan nilai d yang menyatakn satuan detik ke type T}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeTime : integer [0..24], integer [0..59], integer [0..59] --> Time
#   {MakeTime(j,m,d) membentuk sebuah type Time yang terdiri dari j jam, m menit, d detik}

# DEFINISI DAN SPESIFIKASI OPERATOR
# NextNSecond : Time, integer --> Time
#   {NextNSecond(T,n) mengembalikan sebuah time baru setelah n detik dari time T}

# Realisasi
def Time(j,m,d):
    return [j,m,d]
def j(T):
    return T[0]
def m(T):
    return T[1]
def d(T):
    return T[2]
def NextNSecond(T,n):
    if d(T) + n < 60:
        return Time(j(T),m(T),d(T)+n)

    else:
        if d(T) + n == 60 and m(T) + 1 != 0:
            return Time(j(T),m(T)+1,0)   

        elif d(T) + n == 60 and m(T) + 1 == 60 and j(T) + 1 != 24:
            return Time(j(T)+1,0,0)

        elif d(T) + n == 60 and m(T) + 1 == 60 and j(T) + 1 == 24:
            return Time(0,0,0)
        
        else:
            return Time((j(T) + (n//3600) if j(T) + (n//3600) < 24 else j(T) + (n//3600) - 24),(m(T) + (n//60) if m(T) + (n//60) < 60 else m(T) + (n//60) - 60),(d(T) + (n % 3600) if n >= 3600 else d(T) + n % 60))
# APLIKASI
print(NextNSecond((11,22,33),3601))