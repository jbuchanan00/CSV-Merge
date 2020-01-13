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
            firstlist = []
            secondlist = []
            writer = csv.writer(new_file)
            for line in reader:
                firstlist.append(line)
            for line2 in secondreader:
                secondlist.append(line2)
            for i in firstlist:
                for j in secondlist:
                    if(i[0] == j[0]):
                        comrow = i + j
                        writer.writerow(comrow)
