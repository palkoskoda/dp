import matplotlib.pyplot as plt
from spracovanie import *
import pandas as pd
plt.close('all')
from mpl_toolkits.mplot3d import Axes3D
import glob
import os
import csv
import mplcursors
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


podmienka1="4"
df = pd.read_csv('hadzanie.csv', header = 0)
hodiny_stav = pd.read_csv('hodiny_stav.csv', header = 0)


l_z=[]
Ppostrannych=[]

datam=[]

spodna_frekvencia=500
vrchna_frekvencia=60
spodna_frekvencia2=-1
vrchna_frekvencia2=-1
okrem_frekvencie=[50,100]

for filename in glob.glob(os.path.join('traceblok/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
    if "_" not  in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
         if "4"  in filename:   

            nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
            if  otacky==5:
                #z =hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item()
                #z =abs(df[df['nazov']==nazov]['daleko'].item()-1*df[df['nazov']==nazov]['blizko'].item())
                z =abs(df[df['nazov']==nazov]['daleko'].item())
                
                #while z in l_z:
                    #z+=0
                l_z.append(z)
                #print(z)
                print(filename)
                datam.append(filename.split("\\")[-1].split(".")[0])
                prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
                #x,y = furier(depeakf (prud, t, 300, 2, 10)[0], t,500)

                y=furier(prud, t,500)
                #g=[x for ind, x in enumerate(furier_x) if spodna_frekvencia*4 < ind < vrchna_frekvencia*4]
                
                #normalizacia:
                #norm_index=int(otacky*400/6)
                #norm=y[200]
                #y=y/norm
                #g=[x for ind, x in enumerate(y) if ((spodna_frekvencia*4/3*otacky > ind  > vrchna_frekvencia*4/3*otacky) and (spodna_frekvencia2*4/3*otacky > ind or ind > vrchna_frekvencia2*4/3*otacky))]
                #Ppostrannych.append(sum(g))
                Ppostrannych.append(hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item())

fig, ax = plt.subplots()
ind = np.arange(len(Ppostrannych))
width = 0.25
plt.bar(l_z, Ppostrannych, width, bottom=0)
#plt.bar(ind + width, data2, width, bottom=0)
#plt.bar(ind + 2*width, data3, width, bottom=0)

ax.set_title('Závislosť hádzania od motohodín')
#ax.set_xticks(ind + width / 2)
#ax.set_xticklabels([x[:3] for x in datam])

#ax.legend((p1[0], p2[0], p3[0]), ('3000', '5000',"8000"))
ax.autoscale_view()
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(datam[sel.target.index]))
ax.set_xlabel('hádzanie [um]')
ax.set_ylabel('motohodiny [h]')
plt.show()
