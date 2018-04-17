import os
import csv
	
	
def dataAnalysis(dataName):
	result = 0
	
	with open(dataname,"r",newline = "") as f:
	    wr = csv.reader(f)
	    i = 0
	    j = 0
	    AvgS = 0
	    MaxX130 = 0
	    MaxX131 = 0
	    MaxX132 = 0
	    MaxX133 = 0
	    MaxY130 = 0
	    MaxY131 = 0
	    MaxY132 = 0
	    MaxY133 = 0
	    MaxY134 = 0
	    MaxZ130 = 0
	    MaxZ131 = 0
	    MaxZ132 = 0
	    MaxZ133 = 0
	    MaxZ134 = 0
	    MaxZ135 = 0
	    MaxZ136 = 0
	    MaxX80 = 0
	    MaxX81 = 0
	    MaxX82 = 0
	    MaxY80 = 0
	    MaxY81 = 0
	    MaxY82 = 0
	    MaxZ80 = 0
	    MaxZ81 = 0
	    MaxZ82 = 0
	    MaxZ83 = 0
	    MaxZ84 = 0
	    MaxZ85 = 0
	    MaxZ86 = 0
	    MaxZ87 = 0
	       
	    for row in wr:
	        j += 1
	        if j==1:
	            continue
	        frq = float(row[8])
	        if j == 3:      
	            AvgS = frq
	            break   
	
	with open(dataname,"r",newline = "") as f:
	    wr = csv.reader(f)
	    for row in wr:
	        i += 1
	        if i==1:
	            continue
	        elif i > 1250:
	                break
	        frq = float(row[8])
	        FFTX = float(row[9])
	        FFTY = float(row[10])
	        FFTZ = float(row[11])
	       
	        if AvgS > 0.1 and AvgS < 0.15:          
	            if frq == 0.0:
	                if MaxX131 < FFTX:
	                    MaxX131 = FFTX
	                if MaxY130 < FFTY:
	                    MaxY130 = FFTY
	                if MaxZ131 < FFTZ:
	                    MaxZ131 = FFTZ
	            elif frq >= 10 and frq < 30:
	                if MaxX130 < FFTX:
	                    MaxX130 = FFTX
	                if MaxY130 < FFTY:
	                    MaxY130 = FFTY
	                if MaxZ132 < FFTZ:
	                    MaxZ132 = FFTZ
	            elif frq >= 30 and frq < 50:
	                if MaxX130 < FFTX:
	                    MaxX130 = FFTX
	                if MaxY131 < FFTY:
	                    MaxY131 = FFTY
	                if MaxZ133 < FFTZ:
	                    MaxZ133 = FFTZ
	            elif frq >= 50 and frq < 70:
	                if MaxX132 < FFTX:
	                    MaxX132 = FFTX
	                if MaxY132 < FFTY:
	                    MaxY132 = FFTY
	                if MaxZ134 < FFTZ:
	                    MaxZ134 = FFTZ
	            elif frq >= 70 and frq < 90:
	                if MaxX133 < FFTX:
	                    MaxX133 = FFTX
	                if MaxY133 < FFTY:
	                    MaxY133 = FFTY
	                if MaxZ135 < FFTZ:
	                    MaxZ135 = FFTZ
	            elif frq >= 90 and frq < 120:
	                if MaxX130 < FFTX:
	                    MaxX130 = FFTX
	                if MaxY134 < FFTY:
	                    MaxY134 = FFTY
	                if MaxZ136 < FFTZ:
	                    MaxZ136 = FFTZ
	            else:
	                if MaxX130 < FFTX:
	                    MaxX130 = FFTX
	                if MaxY130 < FFTY:
	                    MaxY130 = FFTY
	                if MaxZ130 < FFTZ:
	                    MaxZ130 = FFTZ          
	            
	        elif AvgS > 0.06 and AvgS < 0.1:
	            if frq >= 10 and frq < 20:
	                if MaxX80 < FFTX:
	                    MaxX80 = FFTX
	                if MaxY80 < FFTY:
	                    MaxY80 = FFTY
	                if MaxZ81 < FFTZ:
	                    MaxZ81 = FFTZ
	            elif frq >= 20 and frq < 30:
	                if MaxX80 < FFTX:
	                    MaxX80 = FFTX
	                if MaxY80 < FFTY:
	                    MaxY80 = FFTY
	                if MaxZ82 < FFTZ:
	                    MaxZ82 = FFTZ
	            elif frq >= 30 and frq < 45:
	                if MaxX81 < FFTX:
	                    MaxX81 = FFTX
	                if MaxY81 < FFTY:
	                    MaxY81 = FFTY
	                if MaxZ83 < FFTZ:
	                    MaxZ83 = FFTZ
	            elif frq >= 45 and frq < 55:
	                if MaxX82 < FFTX:
	                    MaxX82 = FFTX
	                if MaxY80 < FFTY:
	                    MaxY80 = FFTY
	                if MaxZ84 < FFTZ:
	                    MaxZ84 = FFTZ
	            elif frq >= 55 and frq < 70:
	                if MaxX80 < FFTX:
	                    MaxX80 = FFTX
	                if MaxY82 < FFTY:
	                    MaxY82 = FFTY
	                if MaxZ85 < FFTZ:
	                    MaxZ85 = FFTZ
	            elif frq >= 95:
	                if MaxX80 < FFTX:
	                    MaxX80 = FFTX
	                if MaxY80 < FFTY:
	                    MaxY80 = FFTY
	                if MaxZ86 < FFTZ:
	                    MaxZ86 = FFTZ
	            else:    
	                if MaxX80 < FFTX:
	                    MaxX80 = FFTX
	                if MaxY80 < FFTY:
	                    MaxY80 = FFTY
	                if MaxZ80 < FFTZ:
	                    MaxZ80 = FFTZ
	
	        else:
	            result += 1
	            break
	
	        
	
	
	if AvgS > 0.1 and AvgS < 0.15:           
	    if MaxX80 > 0.02 or MaxX81 < 0.02 or MaxX82 < 0.11 or MaxX83 < 0.035:
	        result +=1
	
	    if MaxX81 > 0.04 or MaxX82 > 0.25 or MaxX83 > 0.07 :
	        result +=1
	
	    if MaxY80 > 0.02 or MaxY81 < 0.02 or MaxY82 < 0.3 or MaxY83 < 0.02 or MaxY84 < 0.02:
	        result += 1
	
	    if MaxY81 > 0.04 or MaxY82 > 0.08  or MaxY83 > 0.04 or MaxY84 > 0.04:
	        result += 1
	
	    if MaxZ80 > 0.02 or MaxZ81 < 0.02  or MaxZ82 < 0.02 or MaxZ83 < 0.02 or MaxZ84 < 0.19 or MaxZ85 < 0.045 or MaxZ86 < 0.02:
	        result += 1       
	
	    if MaxZ81 > 0.04  or MaxZ82 > 0.04 or MaxZ83 > 0.04 or MaxZ84 > 0.3 or MaxZ85 > 0.08 or MaxZ86 > 0.04:
	        result += 1  
	
	elif AvgS > 0.06 and AvgS < 0.1:
	            
	    if MaxX80 > 0.02 or MaxX81 < 0.11 or MaxX82 < 0.04:
	        result +=1
	
	    if MaxX81 > 0.2 or MaxX82 > 0.06:
	        result +=1
	
	    if MaxY80 > 0.02 or MaxY81 < 0.2 or MaxY82 < 0.025:
	        result += 1
	    
	    if MaxY81 > 0.95 or MaxY82 > 0.04:
	        result += 1
	
	    if MaxZ80 > 0.02 or MaxZ81 < 0.02  or MaxZ82 < 0.02 or MaxZ83 < 0.21 or MaxZ84 < 0.052 or MaxZ85 < 0.02 or MaxZ86 < 0.02:
	        result += 1
	        
	    if MaxZ81 > 0.04 or MaxZ82 > 0.06 or MaxZ83 > 0.5 or MaxZ84 > 0.08 or MaxZ85 > 0.04 or MaxZ86 > 0.04:
	        result += 1
	
	else:
	    result +=1            
	    
	return result
	   