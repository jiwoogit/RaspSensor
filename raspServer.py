import threading
from socket import *
import sys
import csv
import os
import time
import shutil
from Raw2KalFFT import *
from dataAnalysis import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy.linalg as lin


def os_popen(path):
    os.popen(path)

def os_system(path):
    os.system(path)

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def deleteFile(file):
    if os.path.exists(file):
        os.remove(file)



def work(connectSocket, addr):
    try:

        data = connectSocket.recv(1024)
        data = data.decode()


        print("Connecting to" + str())
        all = data.split('/')
        comm = all[0]

        if(comm == "upload"):
            createFolder('downlaod')

            dataName = all[1]
            print("Uploading " + dataName + "...")
            dataTransffered = 0
            
            createFolder('upload')
            deleteFile('upload/' + dataName)
            with open('upload/' +dataName, 'wb') as f:
                data = connectSocket.recv(1024)
                f.write(data)
                dataTransffered += len(data)
                while data:
                    data = connectSocket.recv(1024)
                    f.write(data)
                    dataTransffered += len(data)

            print("Uploading Completed : ", dataTransffered, "bytes...")

        if(comm == "analysis"):
            
            createFolder('result')
            createFolder('data_processed')

            dataName = all[1]
            print("Analysis " + dataName + "...")
            Raw2kalFFT(dataName)
            print("Analysis Completed : " + dataName + "...")

        if(comm == "sending"):

            dataName = "result/" + all[1] + ".csv"
            print("Sending " + dataName + "...")
            result = dataAnalysis(dataName)
            connectSocket.send(result.encode())
            with open("data_processed/" + all[1]+".png", 'r') as f:
                data = f.read(1024).encode()
                while data:
                    connectSocket.send(data)
                    data = f.read(1024).encode()

            print("Sending Completed : " + dataName + "...")




        connectSocket.close()


    except Exception as e:
        print(e)

    return None


try:
    host = ''
    serverPort = 12000

    ADDR = (host, serverPort)
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(ADDR)
    serverSocket.listen(5)
 
    with open("login.csv", 'a', newline ='') as f:
        wr = csv.writer(f)
        wr.writerow(['master', 'master'])




except exception as e:
        print(e)

while(1):
    try:

        connectSocket, addr = serverSocket.accept()

        work(connectSocket, addr)
        """
        t = threading.Thread(target=work, args = (connectSocket, addr))
        t.start()
        t.join()
        """

    except exception as e:
        print(e)

serverSocket.close()

