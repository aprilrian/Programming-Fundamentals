# Nama file: penanggalan.py
# Deskripsi: membuat tipe bentukan Date beserta konstruktor dan selektornya
# Pembuat: Aprilyanto Setiyawan Siburian
# Tanggal: 27 September 2021

#DEFINISI DAN SPESIFIKASI TYPE
# type Hr : integer [1...31]
#   {definisi ini hanyalah untuk “menamakan” type integer dengan nilai tertentu supaya mewakili hari, sehingga jika dipunyai suatu nilai integer, kita dapat memeriksa apakah nilai integer tersebut mewakili Hari yang absah}
# type Bln : integer [1...12]
#   {definisi ini hanyalah untuk “menamakan” type integer dengan daerah nilai tertentu supaya mewakili Bulan}
# type Thn : integer > 0
#   {definisi ini hanyalah untuk “menamakan“ type integer dengan daerah nilai tertentu supaya mewakili tahun}
# type date <d: Hr, m:Bln,y:Thn>
#   {<d,m,y> adalah tanggal d bulan m tahun y}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeDate : <Hr,Bln,Thn> --> date
#   {MakeDate<h,b,t> --> tanggal pada hari, bulan, tahun yang bersangkutan}
# Realisasi dalam Python
class Hr:
    def __init__(self,hari):
        self.hari = hari

class Bln:
    def __init__(self,bulan):
        self.bulan = bulan

class Thn:
    def __init__(self,tahun):
        self.tahun = tahun

class date(Hr,Bln,Thn):
    def __init__(self,hari,bulan,tahun):
        Hr.__init__(self,hari)
        Bln.__init__(self,bulan)
        Thn.__init__(self, tahun)

# DEFINISI DAN SPESIFIKASI SELEKTOR
#  Day : date --> Hr
#   {Day (D) memberikan hari d dari D yang terdiri dari <d,m,y>}
#  Realisasi dalam Python
def Day(D):
    return D.hari if 1 <= D.hari <= 31 else False

 # Month : date --> Bln
 #  {Month (D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
 # Realisasi dalam Python
def Month(D):
    return D.bulan if 1<= D.bulan <=12 else False

 # Year : date --> Thn
 #  {Year (D) memberikan tahun y dari D yang terdiri dari <d,m,y>}
 # Realisasi dalam Python
def Year(D):
    return D.tahun if D.tahun >0 else False

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
# Nextday : date --> date
#  {NextDay(D): menghitung date yang merupakan keesokan hari dari date D yang diberikan}
# Realisasi dalam Python
def Nextday(D):
    if Month(D) == 1 or Month(D) ==3 or Month(D) == 5 or Month(D)==7 or Month(D) == 8 or Month(D) == 10:
        if Day(D)<31:
            return date(Day(D)+1,Month(D),Year(D))
        elif Day(D)==31:
            return date(1,Month(D)+1,Year(D))
    elif Month(D)==2:
        if IsKabisat(D) == True:
            if Day(D)<29:
                return date(Day(D)+1, Month(D), Year(D))
            elif Day(D)==29:
                return date(1,Month(D)+1,Year(D))
        else:
            if Day(D)<28:
                return date(Day(D)+1, Month(D), Year(D))
            elif Day(D)==28:
                return date(1,Month(D)+1, Year(D))
    elif Month(D)==4 or Month(D)==6 or Month(D)==9 or Month(D)==11:
        if Day(D)<30:
            return date(Day(D)+1, Month(D),Year(D))
        elif Day(D)==30:
            return date(1,Month(D)+1,Year(D))
    elif Month(D)==12:
        if Day(D)<31:
            return date(Day(D)+1, Month(D),Year(D))
        elif Day(D)==31:
            return date(1,1,Year(D)+1)
    else:
        return False

# Yesterday : date --> date
#  {Yesterday(D): Menghitung date yang merupakan 1 hari sebelum date D yang diberikan}
# Realisasi dalam Python
def Yesterday(D):
    if Day(D) == 1:
        if Month(D) == 12 or Month(D) == 5 or Month(D) == 7  or Month(D) == 10:
            return date(30, Month(D) - 1, Year(D))
        elif Month(D) == 3:
            if IsKabisat(D)==True:
                return date(29, Month(D)-1,Year(D))
            else:
                return date(28, Month(D)-1, Year(D))
        elif Month(D)==2 or Month(D) == 4 or Month(D) == 6 or Month(D)==8 or Month(D) == 9 or Month(D) == 11:
            return date(31, Month(D)-1, Year(D))
        elif Month(D) == 1:
            return date(31, 12, Year(D) - 1)
    else:
        return date(Day(D) - 1, Month(D), Year(D))

# NextNday : date, integer --> date
#   {NextNDay(D,N) : Menghitung date yang merupakan N hari (N adalah nilai integer) sesudah dari date D yang diberikan}
def NextNday(D,N):
    if N ==1:
        return Nextday(D)
    else:
        return NextNday(Nextday(D),N-1)

# dpm : date --> integer
#   {dpm(b) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. terhitung mulai satu januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan b, tanpa memperhhitungkan tahun kabisat}
# Realisasi dalam Python
def dpm(b):
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 60
    elif b == 4:
        return 91
    elif b == 5:
        return 121
    elif b == 6:
        return 152
    elif b == 7:
        return 182
    elif b == 8:
        return 213
    elif b == 9:
        return 244
    elif b == 10:
        return 274
    elif b == 11:
        return 305
    elif b == 12:
        return 335
    else:
        return "Tidak Valid"

# HariKe1900: date --> integer [0..366]
#   {HariKe1900(D) : Menghitung jumlah hari terhadap 1 Januari pada tahun y, dengan memperhitungkan apakah y adalah tahun kabisat}
# Realisasi dalam Python
def HariKe1900(D):
    return Day(D) + dpm(Month(D)) if Month(D) > 2 and IsKabisat(D) == True else Day(D) - 1 + dpm(Month(D))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEbD : 2 date → boolean
#  {IsEbD(d1,d2) benar jika d1=d2, mengirimkan true jika d1=d2 and m1=m2 and y1=y2}
# Realisasi dalam Python
def IsEbD(D1,D2):
    return HariKe1900(D1) == HariKe1900(D2) and Year(D1)== Year(D2)

# IsBefore : 2 date → boolean
#  {IsBefore(d1,d2) benar e jika d1 adalah sebelum d2 mengirimkan true jika D1 adalah "sebelum" D2}
# Realisasi dalam Python
def IsBefore(D1,D2):
    if Year(D1)<Year(D2):
        return True
    elif Year(D1) == Year(D2):
        return True if HariKe1900(D1) < HariKe1900(D2) else False
    else:
        return False

# IsAfter : 2 date → boolean
#  {IsAfter(d1,d2) benar jika d1 adalah sesudah d2 mengirimkan true jika D1 adalah "sesudah" D2: HariKe1900 dari D1 adalah lebih besar dari HariKe1900 dari D2.}
# Realisasi dalam Python
def IsAfter(D1,D2):
    if Year(D1)>Year(D2):
        return True
    elif Year(D1)==Year(D2):
        return True if HariKe1900(D1) > HariKe1900(D2) else False
    else:
        return False

# IsKabisat : integer → boolean
#   {IsKabisat(a) true jika tahun 1900+a adalah tahun kabisat: habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400}
# Realisasi dalam Python
def IsKabisat(D):
    return True if (Year(D) % 4 == 0 and Year(D)%100 !=0) or Year(D)%400 == 0 else False

# Aplikasi
a = date(16,11,2003)
b = date(1,7,2000)
print(IsKabisat(date(1,7,2000)))
print(Day(b))
print(Month(b))
print(Year(b))
print("{},{},{}".format(Day(Nextday(b)),Month(Nextday(b)),Year(Nextday(b))))
print("{},{},{}".format(Day(Yesterday(b)),Month(Yesterday(b)),Year(Yesterday(b))))
print(HariKe1900(a))
print(IsEbD(a,b))
print(IsBefore(a,b))
print(IsAfter(a,b))
print(IsKabisat(a))
print(IsKabisat(b))
print("{},{},{}".format(Day(NextNday(a,10)),Month(NextNday(a,10)),Year(NextNday(a,10))))
