import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy.linalg as lin
import os

def deleteFile(file):
    if os.path.exists(file):
        os.remove(file)

def Raw2kalFFT(fileName):
	#Rearranging Data into a given format

	rawData = pd.read_csv("upload/"+fileName).values
	sampleTime = rawData[2,0]-rawData[1,0]
	
	
	d = {'time':rawData[:,0], 'AccX':rawData[:,1], 'AccY':rawData[:,2], 'AccZ':rawData[:,3]}
	df = pd.DataFrame(data=d)
	df = df[['time','AccX','AccY','AccZ']]
	
	#Applying Kalman Filter to rawData
	
	FiltAccX = np.zeros(len(df.time))
	FiltAccY = np.zeros(len(df.time))
	FiltAccZ = np.zeros(len(df.time))
	
	xavg = np.average(df.AccX)
	yavg = np.average(df.AccY)
	zavg = np.average(df.AccZ)
	
	dt = sampleTime
	A = np.array([[1, dt], [0, 1]])   #Response Time but higher noise
	H = np.array([[1,0]])          #Amplitude
	Q = np.array([[1,0],[0,1]])
	R = 1
	
	x = np.array([[0],[20]])
	P = 3*np.eye(2)
	
	for i in np.arange(0,len(df.time)):        
	    xp = np.dot(A, x)
	    Pp = np.dot(np.dot(A, P), A.T) + Q
	    
	    K = np.dot(np.dot(Pp, H.T), lin.inv(np.dot(np.dot(H, Pp), H.T) + R))
	    
	    x = xp + K * (df.AccX[i] - np.dot(H, xp))
	    P = Pp - np.dot(np.dot(K, H), Pp)
	
	    FiltAccX[i] = x[1]
	df['FiltAccX'] = FiltAccX
	
	
	for i in np.arange(0,len(df.time)):        
	    xp = np.dot(A, x)
	    Pp = np.dot(np.dot(A, P), A.T) + Q
	    
	    K = np.dot(np.dot(Pp, H.T), lin.inv(np.dot(np.dot(H, Pp), H.T) + R))
	    
	    x = xp + K * (df.AccY[i] - np.dot(H, xp))
	    P = Pp - np.dot(np.dot(K, H), Pp)
	
	    FiltAccY[i] = x[1]
	df['FiltAccY'] = FiltAccY
	
	xz = np.array([[0],[20]])
	Pz = 3*np.eye(2)
	
	for i in np.arange(0,len(df.time)):        
	    xp = np.dot(A, xz)
	    Pp = np.dot(np.dot(A, Pz), A.T) + Q
	    
	    K = np.dot(np.dot(Pp, H.T), lin.inv(np.dot(np.dot(H, Pp), H.T) + R))
	    
	    xz = xp + K * (df.AccZ[i] - np.dot(H, xp))
	    Pz = Pp - np.dot(np.dot(K, H), Pp)
	
	    FiltAccZ[i] = xz[1]
	df['FiltAccZ'] = FiltAccZ
	
	df = df[2000:4500]
	t = df.time
	n= len(t)
	
	xdat = df.FiltAccX
	ydat = df.FiltAccY
	zdat = df.FiltAccZ
	
	
	# FFT
	Fs = 1/sampleTime
	
	k = np.arange(n)
	T = n/Fs
	freq = k/T
	
	
	xfft = 2*(np.fft.fft(xdat)/n).T
	yfft = 2*(np.fft.fft(ydat)/n).T
	zfft = 2*(np.fft.fft(zdat)/n).T
	
	df['Frequency'] = freq
	df['FFTAccX'] = abs(xfft.real)
	df['FFTAccY'] = abs(yfft.real)
	df['FFTAccZ'] = abs(zfft.real)
	outputName = "result/" + fileName[:fileName.rfind('.')+1] + "csv"
	df.to_csv(outputName)


	#Calculate maximum values  (for plotting purpose)
	rawData2 = pd.read_csv("result/"+fileName).values
	
	dmax = {'AccX':rawData[2000:4500,1].T, 'AccY':rawData[2000:4500,2].T, 'AccZ':rawData[2000:4500,3].T, 'FiltAccX':FiltAccX[2000:4500], 'FiltAccY':FiltAccY[2000:4500], 'FiltAccZ':FiltAccZ[2000:4500]}
	dfmax = pd.DataFrame(data=dmax)
	Max_Value = dfmax.max().max()
	print(Max_Value)

	dmax2 = {'FFTAccX':rawData2[2000:4500,9].T, 'FFTAccY':rawData2[2000:4500,10].T, 'FFTAccZ':rawData2[2000:4500,11].T}
	dfmax2 = pd.DataFrame(data=dmax2)
	Max_amp_FFT = dfmax2.max().max()
	print(Max_amp_FFT)

	start_time = rawData[2000,0]
	elapsed_time = rawData[4500,0]
	end_frequency = rawData2[-1,8]
	print(elapsed_time)
	
	# Plot 3 time domain graphs and 3 frequency domain graphs
	
	
	plt.figure(figsize=(15,8))

	
	plt.subplot(231)
	plt.plot( df.time, df.AccX-xavg, 'g',
	         df.time, df.FiltAccX, 'r')
	plt.xlim(start_time,elapsed_time)
	plt.ylim(-Max_Value,Max_Value)
	plt.xlabel('time (s)', size=8)
	plt.ylabel('AccX', size=8)
	plt.title('Kalman Filtered Data X', size=8)
	plt.legend(['Raw Data','Kalman'], loc=1)
	plt.grid(True)
	
	plt.subplot(232)
	plt.plot( df.time, df.AccY-yavg, 'g',
	          df.time, df.FiltAccY, 'r')
	plt.xlim(start_time,elapsed_time)
	plt.ylim(-Max_Value,Max_Value)
	plt.xlabel('time (s)', size=8)
	plt.ylabel('AccY', size=8)
	plt.title('Kalman Filtered Data Y', size=8)
	plt.legend(['Raw Data','Kalman'], loc=1)
	plt.grid(True)
	
	plt.subplot(233)
	plt.plot( df.time, df.AccZ-zavg, 'g',
	          df.time, df.FiltAccZ, 'r')
	plt.xlim(start_time,elapsed_time)
	plt.ylim(-Max_Value,Max_Value)
	plt.xlabel('time (s)', size=8)
	plt.ylabel('AccZ', size=8)
	plt.title('Kalman Filtered Data Z', size=8)
	plt.legend(['Raw Data','Kalman'], loc=1)
	plt.grid(True)
	
	
	plt.subplot(234)
	plt.plot(freq, abs(xfft.real))
	plt.xlim(0,end_frequency/2)
	plt.ylim(0,2*Max_amp_FFT)
	plt.xlabel('freq (Hz)', size=8)
	plt.ylabel('Amp. |X|', size=8)
	plt.title('FFT Analysis of AccX', size=8)
	plt.grid(True)
	
	plt.subplot(235)
	plt.plot(freq, abs(yfft.real))
	plt.xlim(0,end_frequency/2)
	plt.ylim(0,2*Max_amp_FFT)
	plt.xlabel('freq (Hz)', size=8)
	plt.ylabel('Amp. |Y|', size=8)
	plt.title('FFT Analysis of AccY', size=8)
	plt.grid(True)
	
	plt.subplot(236)
	plt.plot(freq, abs(zfft.real))
	plt.xlim(0,end_frequency/2)
	plt.ylim(0,2*Max_amp_FFT)
	plt.xlabel('freq (Hz)', size=8)
	plt.ylabel('Amp. |X|', size=8)
	plt.title('FFT Analysis of AccZ', size=8)
	plt.grid(True)
	

	
	jpgName = "data_processed/" + fileName[:fileName.rfind('.')+1] + "png"
	deleteFile(jpgName)
	plt.savefig(jpgName, bbox_inches='tight')
	
	
	deleteFile(outputName)
	df.to_csv(outputName)
	#deleteFile("temp.csv")
	
if __name__ == "__main__":
    Raw2kalFFT("TEST 10.csv")