from MPU6050 import MPU6050
from time import *
import csv
import time 
import pandas as pd


timestep = 0.1
max = 10

try:

    userName = "sample"
    pw = '111'

    sensor = MPU6050(0x68)
    start_time = time()

except Exception as e:
    print(e)

time=0
while time<max:

    try:
        prev_time = time()

        accel_data = sensor.get_accel_data()

        x = accel_data['x']
        y = accel_data['y']
        z = accel_data['z']

        value = []

        value.append([x, y, z])
        
        sleep(timestep)

        time += timestep

        post_time = time()
        print("each level time : " + (post_time - prev_time))
    except Exception as e:
        print(e)
            
try:
    with open(userName + "_data.csv" , 'a', newline = '') as g:
        wr = csv.writer(g)
        for i in value:
            wr.writerow(i)

    end_time = time()

    print (end_time - start_time)

except Exception as e:
    print(e)

d = {'time':(np.arange(0,len(rawData)*sampleTime,sampleTime)), 'AccX':rawData[:,0], 'AccY':rawData[:,1], 'AccZ':rawData[:,2]}
df = pd.DataFrame(data=d)
df = df[['time','AccX','AccY','AccZ']]


df.to_csv('crush 1_data_processed.csv')