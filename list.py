# DEFINISI DAN SPESIFIKASI TYPE
# {Konstruktor menambahkan elemen di awal, notasi prefix}
# type List : [ ], atau [e o List]
# {Konstruktor menambahkan elemen di akhir, notasi postfix}
# type List : [ ] atau [List • e]
# {Definisi List : sesuai dengan definisi rekursif di atas}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso : elemen, List -> List
# {Konso(E,L): menghasilkan sebuah list dari e dan L, dengan e sebagai elemen pertama e: e o L  L'}
# Konsi : List, elemen -> List
# { Konsi(L,E):  menghasilkan sebuah list  dari L  dan e,  dengan e sebagai  elemen terakhir  list :	L • e  L'}

# DEFINISI DAN SPESIFIKASI SELEKTOR O
# FirstElmt: List tidak kosong -> elemen
# {FirstElmt(L) Menghasilkan elemen pertama list L}

# Tail : List tidak kosong -> List
# {Tail(L) : Menghasilkan list tanpa elemen pertama list L, mungkin kosong}

# LastElmt : List tidak kosong -> elemen
# {LastElmt(L) : Menghasilkan elemen terakhir list L}

# Head : List tidak kosong -> List
# {Head(L) : Menghasilkan list tanpa elemen terakhir list L, mungkin kosong}

# DEFINISI DAN SPESIFIKASI PREDIKAT DASAR (UNTUK BASIS ANALISA REKURENS)
# {Basis 0 }
# IsEmpty : List -> boolean
# {IsEmpty(L) benar jika list kosong }

# {Basis 1 }
# IsOneElmt: List -> boolean
# {IsOneElmt (X,L) adalah benar jika list L hanya mempunyai satu elemen }

# DEFINISI DAN SPESIFIKASI PREDIKAT RELASIONAL
# IsEqual : 2 List -> boloean
# {IsEqual (L1,L2) benar jika semua elemen list L1 sama dengan L2: sama urutan dan sama nilainya }

# BEBERAPA DEFINISI DAN SPESIFIKASI FUNGSI LAIN
# NbElmt : List  -> integer
# {NbElmt(L) : Menghasilkan banyaknya elemen list, nol jika kosong }

# Copy : List  -> List
# {Copy(L) : Menghasilkan list yang identik dengan list asal}

# Inverse : List  -> List
# {Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah kebalikan dari list asal}


def FirstElmt(T):
    if not IsEmpty(T):
        return T[0]
    else:
        return []
    
def LastElmt(L):
    if not IsEmpty(L):
        return L[-1]
    else:
        return []

def Tail(T):
    if not IsEmpty(T):
        return T[1:]
    else:
        return []

def Head(L):
    if not IsEmpty(L):
        return L[:-1]
    else:
        return []

def Konso(E,L):
    if E==[]:
        return L
    elif L==[]:
        return [E]
    else:
        return [E]+L
    
def Kons(E,L):
    if E==[]:
        return L
    elif L==[]:
        return [E]
    return L+[E]

def IsEmpty(L):
    return L==[]

def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L)==X:
            return True
        else:
            return IsMember(X,Tail(L))

def IsEqual(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    elif IsEmpty(L1) and not IsEmpty(L2):
        return False
    elif IsEmpty(L2) and not IsEmpty(L1):
        return False
    elif FirstElmt(L1)==FirstElmt(L2):
        return IsEqual(Tail(L1),Tail(L2))
    else:
        return False


def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))


def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Kons(Inverse(Tail(L)),FirstElmt(L))

