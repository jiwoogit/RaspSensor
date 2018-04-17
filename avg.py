import csv
import os
import math

def deleteFile(file):
    if os.path.exists(file):
        os.remove(file)

a=1
b=64

deleteFile("RMS.csv")
deleteFile("AVG.csv")

Frq = []
FFTx = []
FFTy = []
FFTz = []

for i in range(2500):
    Frq.append(0)
    FFTx.append(0)
    FFTy.append(0)
    FFTz.append(0)
try:
    for i in range(a, b):
        j= 0
        dataName = "tc/0.13/H.C 0.13 "+ str(i) + ".csv"
        with open(dataName, 'r', newline = '') as f:
            gg = csv.reader(f)
            for row in gg:
                if(row[8].isalpha()):
                    continue
                Frq[j] += math.pow(float(row[8]), 2)
                FFTx[j] += math.pow(float(row[9]), 2)
                FFTy[j] += math.pow(float(row[10]), 2)
                FFTz[j] += math.pow(float(row[11]), 2)
                j+=1
        print("{0:.2f}% completed".format(i*100/(b-a)))
    for i in range(2500):
        Frq[i] = math.sqrt(Frq[i] / (b-a))
        FFTx[i] = math.sqrt(FFTx[i] / (b-a))
        FFTy[i] = math.sqrt(FFTy[i] / (b-a))
        FFTz[i] = math.sqrt(FFTz[i] / (b-a))


    with open("RMS.csv", 'a',newline = '') as g:
        gg = csv.writer(g)
        for i in range(2500):
            gg.writerow([Frq[i], FFTx[i], FFTy[i], FFTz[i]])


except Exception as e:
    print(e)


Frq = []
FFTx = []
FFTy = []
FFTz = []

for i in range(2500):
    Frq.append(0)
    FFTx.append(0)
    FFTy.append(0)
    FFTz.append(0)
try:
    for i in range(a, b):
        j= 0
        dataName = "tc/0.13/H.C 0.13 "+ str(i) + ".csv"
        with open(dataName, 'r', newline = '') as f:
            gg = csv.reader(f)
            for row in gg:
                if(row[8].isalpha()):
                    continue
                Frq[j] += float(row[8])
                FFTx[j] += float(row[9])
                FFTy[j] += float(row[10])
                FFTz[j] += float(row[11])
                j+=1
        print("{0:.2f}% completed".format(i*100/(b-a)))
    for i in range(2500):
        Frq[i] = Frq[i] / (b-a)
        FFTx[i] = FFTx[i] / (b-a)
        FFTy[i] = FFTy[i] / (b-a)
        FFTz[i] = FFTz[i] / (b-a)


    with open("AVG.csv", 'a',newline = '') as g:
        gg = csv.writer(g)
        for i in range(2500):
            gg.writerow([Frq[i], FFTx[i], FFTy[i], FFTz[i]])


except Exception as e:
    print(e)