from tkinter import *
from tkinter.filedialog import askopenfilename
import csv

Tk().withdraw()
filename = askopenfilename()

Tk().withdraw()
secondfile = askopenfilename()
NewFileName = input("What is the new file name?")

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    with open(secondfile) as newcsvfile:
        secondreader = csv.reader(newcsvfile)
        with open(NewFileName, 'w') as new_file:
            #writer = csv.writer(new_file)
            for line in reader:
                
                print(line)
            for line in secondreader:
                
                print(line)
    
