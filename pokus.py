import sys
from msvcrt import getch

def printXY(progress):
    """ahoj"""
    a=0
    for i in range(10000):
        a=a*5
    sys.stdout.write("Download progress: %d%%\r" %(progress)) # to umoznuje zapis do jedne radky. Nejak je mozno nastavit i sloupce. Nuntou prozkoumat. Mozno bude lepsi pouzit Tkinter
    sys.stdout.flush()

def print_start():
    """
    Tato funkce vytiskne uvodni hlavicku skriptu.

    """
    print
    print "***********************************"
    print "                Start              "
    print "-----------------------------------"

def print_end():
    print
    print "                Konec              "
    print "***********************************"
    print

def tiskni_hvezdicky(pocet):
    for radek in range(pocet+1):
        for sloupec in range(radek):
            sys.stdout.write('*')
            sys.stdout.flush()
        print

def pascal_trojuh(pocet):
    """
    Vypocet Fiboniace
    """
    pole=[0 for i in range (30)] # priprav si prazdne pole
    pole[0]=1
    pole[1]=0
    pole[2]=0
    pole[3]=0
    pole1 = [0 for i in range (30)]
    for i in range(30):
        if i==0:
           pole1[0]=1
        if i>0 and i<4:
            pole1[i]=pole[i-1]+pole[i]
    print pole1




if __name__ == '__main__':
    print_start()
    print "Umisteni skriptu: " + sys.path[0] #print (print_start.__doc__) # tohle umi vytisknout napovedu/dokumentaci funkce
    
    pascal_trojuh(5)
    #    printXY(100) # vytiskni dane cislo na pozici
    #tiskni_hvezdicky(10)

    print
     # cekej na stisk klavesy, q = quit
 #   key="" # zde se uklada stisknuta klavesa
 #   while key!="q":
 #       print "Stiskni 'q'  pro ukonceni programu."
 #       key = getch()
 #       print(key)

    print_end()# komentar pomoci multi line edit
