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


if __name__ == '__main__':
    print_start() 
    print "Umisteni skriptu: " + sys.path[0]
    #print (print_start.__doc__) # tohle umi vytisknout napovedu/dokumentaci funkce
    
    #    printXY(100) # vytiskni dane cislo na pozici
    for radek in range(10):
        for sloupec in range(radek):
            sys.stdout.write('*')
            sys.stdout.flush()
            
        print
    print
     # cekej na stisk klavesy, q = quit
 #   key="" # zde se uklada stisknuta klavesa
 #   while key!="q": 
 #       print "Stiskni 'q'  pro ukonceni programu."
 #       key = getch()
 #       print(key)

    print_end()# komentar pomoci multi line edit

