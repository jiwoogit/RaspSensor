from socket import *
from time import *
import csv

max = 5000
fileNum = 10

serverName = '115.145.202.17'

try:

    serverPort = 12000
    ADDR = (serverName, serverPort)

    for i in range(1, 2):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(ADDR)

        fileName = "TEST " + str(i) + ".csv"
        msg = "analysis/" + fileName

        clientSocket.send(msg.encode())
        #print("fafa")

        

        print("Send Complete : " + fileName + " ...")

        clientSocket.close()


except Exception as e:
    print(e)
