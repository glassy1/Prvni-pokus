import sys
from msvcrt import getch

def printXY(progress):
    """ahoj"""
    a=0
    for i in range(100000):
        a=a*5
    sys.stdout.write("Download progress: %d%%\r" %(progress)) # to umoznuje zapis do jedne radky. Nejak je mozno nastavit i sloupce. Nuntou prozkoumat. Mozno bude lepsi pouzit Tkinter
    sys.stdout.flush()

for i in range(10):
    printXY(i) # vytiskni dane cislo
print
key="" # zde se uklada stisknuta klavesa
while key!="q": # cekej na stisk klavesy
    print "Stiskni 'q'  pro ukonceni programu."
    key = getch()
    print(key)