import sys

def printXY(progress):
    """ahoj"""
    a=0
    for i in range(100000):
        a=a*5
    sys.stdout.write("Download progress: %d%%\r" %(progress)) # to umoznuje zapis do jedne radky. Nejak je mozno nastavit i sloupce. Nuntou prozkoumat. Mozno bude lepsi pouzit Tkinter
    sys.stdout.flush()

for i in range(1000):
    printXY(i)
