# Nama file : modules_list.py
# Deskripsi : Modules yang dipakai di List
# Pembuat : Aprilyanto Setiyawan Siburian
# Tanggal : 31 Oktober 2021

# prec : integer --> integer
#   {prec(n) adalah representasi minimal mesin}

def prec(n):
    return n-1

# succ : integer --> integer
#   {succ(n) adalah representasi maksimal mesin}

def succ(n):
    return n+1

# Konso : elemen, list --> list
#   {Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama e : e o L -> L'}

def Konso(e,L):
    if L == []:
        return [e]
    else:
        return [e]+L

# Konsi : elemen, list --> list
#   {Konsi(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen terakhir dari List, 
#    e : L o e -> L'}

def Konsi(L,e):
    if L == []:
        return [e]
    else:
        return L + [e]

# Head : list tidak kosong --> list
#   {Head(L) menghasilkan list tanpa elemen terkahir / nilai terkahir, mungkin kosong}

def Head(L):
    return L[:-1]

# Tail : list tidak kosong --> list
#   {Tail(L) menghasilkan list tanpa elemen pertama / nilai pertama, mungkin kosong}

def Tail(L):
    return L[1:]

# FirstElmt : list tidak kosong --> elemen
#   {FirstElmt (L) mengeluarkan elemen pertama dari L yang berupa List}

def FirstElmt(L):
    if L != []:
        return L[0]
    
# LastElmt : list tidak kosong --> elemen
#   {LastElmt (L) mengeluarkan elemen terakhir dari L yang berupa List}

def LastElmt(L):
    if L != []:
        return L[-1]

# IsEmpty : list --> boolean
#   {IsEmpty(L) True jika L adalah sebuah list kosong, L = []}

def IsEmpty(L):
    return L == []

# NbElmt(L) : list --> integer
#   {NbElmt(L) menghasilkan banyaknya elemen list, nol jika kosong}

def NbElmt(L):
    if L == []:
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# IsOneElmt : list --> boolean
#   {IsOneElmt(L) adalah benar jika list hanya mempunyai satu elemen}

def IsOneElmt(L):
    return NbElmt(L) == 1

# IsEqual : 2 List → boolean
#   {IsEqual (L1,L2) benar jika semua elemen list L1 sama dengan L2: sama urutan dan 
#   sama nilainya}

def IsEqual(L1,L2):
    if NbElmt(L1) == NbElmt(L2):
        if L1 == [] and L2 == []:
            return True
        elif FirstElmt(L1) != FirstElmt(L2):
            return False
        else:
            return FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1),Tail(L2))
    else:
        return False

# IsMember: elemen, List --> boolean
#   {IsMember(x,L) adalah benar jika x adalah elemen list L}

def IsMember(x,L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L)==x:
            return True
        else:
            return IsMember(x,Tail(L))

# ElmtkeN : integer, List tidak kosong --> elemen
#   {ElmtKeN(n,L) menghasilkan elemen ke-n  list L, n ≥  0, dan n ≤ banyaknya elemen list}

def ElmtKeN(n,L):
    if n == 1:
        return FirstElmt(L)
    else:
        return ElmtKeN(prec(n),Tail(L)) 
    
# Copy : List --> List
#   {Copy(L) menghasilkan salinan list L, artinya list lain yang identik dengan L}

def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L),Copy(Tail(L)))
        
# Inverse : List → List 
#   {Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah 
#    kebalikan dari list asal} 

def Inverse(L):
    if L == []:
        return []
    else:
        return Konso(LastElmt(L),(Inverse(Head(L))))
    
# Concat : List --> List
#   {Concat(L1,L2) menghasilkan konkatenasi (gabungan) list L1 dan L2}
def Concat(L1,L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1),Concat(Tail(L1),L2))
    
# IsNbElmtN : List, integer >= 0 --> integer
#   {IsNbElmtN(L,n) true jika banyaknya elemen list sama dengan n}
def IsNbElmtN(L,n):
    if n == 0:
        if IsEmpty(L):
            return True 
        else:
            return False
    else:
        IsNbElmtN(Tail(L),prec(n))

# IsXElmtKeN : elemen, integer ≥ 0, List (tidak kosong) --> boolean
#   {IsXElmtKeN(x,n,L) true jika x adalah elemen ke-n list L, n ≥  0, dan n ≤ banyaknya elemen list}

def IsXElmtKeN(x,n,L):
    if IsMember(x,L):
        if n == 1 and FirstElmt(L) == x:
            return True
        else:
            return False or IsXElmtKeN(x,prec(n),Tail(L))
    else:
        return False
   
# IsInverse : 2 List --> boolean
#   {IsInverse(L1,L2) true jika L2 adalah list dengan urutan elemen terbalik dari L1}
    
def IsInverse(L1,L2):
    if NbElmt(L1) == NbElmt(L2):
        if IsEmpty(L1) and IsEmpty(L2):
            return True
        else:
            return (FirstElmt(L1) == LastElmt(L2)) and IsInverse(Head(Tail(L1)),Head(Tail(L2)))
    else:
        return False