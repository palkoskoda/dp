import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy import signal

def depeakf (data, t, fs, pocet, order):
    vykon=data
    yf = scipy.fftpack.fft(data)
    xf = np.linspace(0.0, (1.0*fs)/(2.0), len(t)/2)
    b=2.0/len(t) * np.abs(yf[:len(t)//2])
    a=np.argsort(b)
    j=0
    for i in range(pocet):
        while (xf[a[-2-i-j]]) < 1:
            j +=1
        vykon = iirnotch_filter(vykon, (xf[a[-2-i-j]]), fs, order)
    #print ("Priemerný prúd je:") 
    #print (b[a[-1]]/2)#prva harmonicka /2
    
    return vykon, (b[a[-1]]/2)    
    
def furier2 (data, t, fs):
    yf = scipy.fftpack.fft(data)
    xf = np.linspace(0.0, (1.0*fs)/(2.0), len(t)/2)
    b=2/len(t) * np.abs(yf[:len(t)//2])  
    return b, xf    

def furier (data, t, fs):
    yf = scipy.fftpack.fft(data)
    xf = np.linspace(0.0, int((1.0*fs)/(2.0)), int(len(t)/2))
    b=2.0/len(t) * np.abs(yf[:len(t)//2])  
    return b#, xf    


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = signal.butter(order, 2*cutoff/fs, 'low') #first parameter is signal order and the second one refers to frequenc limit. I set limit 30 so that I can see only below 30 frequency signal component
    y = signal.filtfilt(b, a, data)
    
    return y

def subor_priemer(nazov):
    data1 = []
    data2 = []
    cas_merania=30

    with open("traceblok/"+ nazov +".ST1", 'r') as file:
        sucet1=0
        sucet2=0
        for line in file:
            if "P 113:  " in line:
                cas_merania=int(line[7:].replace('\n',''))/1000
            if "@Messwerte Trace: 17" in line:
                stlpec=1
            if "@Messwerte Trace: 18" in line:
                stlpec=2
            if "M " in line:
                x= (line[3:].replace('\n','').split(': '))
                if stlpec==1:
                    data1.append(float(x[1]))
                    sucet1+=float(x[1])
                if stlpec==2:
                    sucet2+=float(x[1])
                    
        if sucet1<sucet2:
            prud=sucet1/len(data1)*-1
        else:
            prud=sucet2/len(data1)*-1
    return prud

def iirnotch_filter(data, cutoff, fs, order=5):
    b, a = signal.iirnotch(cutoff/(fs/2), order)
    y = signal.lfilter(b, a, data)
    return y

def subor_prud(nazov):
    prud = []
    vykon= []
    t=[]
    cas_merania=30

    with open("traceblok/"+ nazov +".ST1", 'r') as file:
        sucet1=0
        sucet2=0
        for line in file:
            if "P 113:  " in line:
                cas_merania=int(line[7:].replace('\n',''))/1000
            if "@Messwerte Trace: 17" in line:
                stlpec=1
            if "@Messwerte Trace: 18" in line:
                stlpec=2
            if "M " in line:
                x= (line[3:].replace('\n','').split(': '))
                if stlpec==1:
                    prud.append(float(x[1]))  
                    sucet1+=float(x[1])
                if stlpec==2:
                    vykon.append(float(x[1]))
                    sucet2+=float(x[1])
                    t.append((int(x[0])*cas_merania)/len(prud))
                    
        if sucet1<sucet2:
            return prud,t
        else:
            return vykon,t
    #return prud, t

def subor(nazov, dpfv, svf):
    prud = []
    vykon= []
    t=[]
    cas_merania=30

    with open("traceblok/"+ nazov +".ST1", 'r') as file:
        sucet1=0
        sucet2=0
        for line in file:
            if "P 113:  " in line:
                cas_merania=int(line[7:].replace('\n',''))/1000
            if "@Messwerte Trace: 17" in line:
                stlpec=1
            if "@Messwerte Trace: 18" in line:
                stlpec=2
            if "M " in line:
                x= (line[3:].replace('\n','').split(': '))
                if stlpec==1:
                    prud.append(float(x[1])*-1)    
                    sucet1+=float(x[1])

                if stlpec==2:
                    vykon.append(float(x[1]))
                    sucet2+=float(x[1])
                    t.append((int(x[0])*cas_merania)/len(prud))
                
    fs = len(prud)/cas_merania  # Sample frequency (Hz)      
    if sucet1<sucet2:
        vykon=prud
        
    vykon, pavg= depeakf(vykon, t, fs, dpfv, 12)
    if svf>5:
        vykon = signal.savgol_filter(vykon, svf, 3)
    
    return vykon[10:],t[10:], pavg, nazov

def vypis_subor(nazov):
    vykon, t, pavg, nazov =subor(nazov, dpfv, svf)
    plt.plot(t, vykon, label=str(nazov)[:6]+" - "+str(round(pavg,2))+"A")
    return


def hlavicka(dpfv_in,svf_in):
    plt.figure()  
    global dpfv
    global svf        
    dpfv=dpfv_in #iirnotch_filter odfiltruje najsilnejšie harmonicke
    svf=svf_in #savgol_filter vyhladí krivku
    return

def pata(otacky):
    plt.legend(loc='center right', shadow=True, fontsize='x-large', )
    plt.title(str(otacky)+" otáčok")
    plt.xlabel("čas [s]")
    plt.ylabel("Prúd [A]")
    return