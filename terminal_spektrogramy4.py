import matplotlib.pyplot as plt
from spracovanie import *
import pandas as pd
plt.close('all')
from mpl_toolkits.mplot3d import Axes3D
import glob
import os
import csv
#import mplcursors
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

def limitmax(inputx, maxvalue):
    if inputx > maxvalue:
        return maxvalue
    if inputx<=maxvalue:
        return inputx
podmienka1="4"
df = pd.read_csv('hadzanie.csv', header = 0)
hodiny_stav = pd.read_csv('hodiny_stav.csv', header = 0)

#fig = plt.figure()
plt.rcParams["figure.figsize"] = 12.6, 6.6
#ax = fig.add_subplot(111, projection='3d')
ax = plt.axes( projection='3d')

sirka = np.arange(0.01,0.2,0.01)
datam=[]
for sirkax  in sirka:
    l_z=[]
    Ppostrannych=[]
    for filename in glob.glob(os.path.join('traceblok/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
        if "_" not  in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)           
            if "4"  in filename:   
                nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
            if  otacky==3:
                #z =hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item()
                z =abs(df[df['nazov']==nazov]['daleko'].item()-1*df[df['nazov']==nazov]['blizko'].item())
                #z =abs(df[df['nazov']==nazov]['blizko'].item())
                
                while z in l_z:
                    z+=0.3
                l_z.append(z)
                #print(z)
                #print(filename)
                datam.append(filename.split("\\")[-1].split(".")[0])
                prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
                x,y = furier2(depeakf (prud, t, 300, 2, 10)[0], t,500)
                #ax.plot(x[:], signal.savgol_filter(np.log(y[:]), 51,3), zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                #ax.plot(x[:], np.log(y[:]), zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                #ax.plot(x, y, zs=z, zdir='y', alpha=0.8)
                #print(otacky*100/6-otacky*sirka*100/6)
                #print(otacky*100/6+otacky*sirka*100/6)
                Ppostrannych.append(sum(furier2(butter_bandpass_filter(depeakf (prud, t, 300, 2, 10)[0], otacky*100/6-otacky*sirkax*100/6, limitmax((otacky*100/6+otacky*sirkax*100/6),150), 300, order=6), t,500))[0])

    #plt.bar(l_z, Ppostrannych, width, bottom=0)
    ax.plot(l_z, Ppostrannych, zs=sirkax, zdir='y', alpha=1,linestyle='none')
#plt.bar(ind + width, data2, width, bottom=0)
#plt.bar(ind + 2*width, data3, width, bottom=0)

ax.set_title('Prúd v závislosti od otáčok')
#ax.set_xticks(ind + width / 2)
#ax.set_xticklabels([x[:3] for x in datam])

#ax.legend((p1[0], p2[0], p3[0]), ('3000', '5000',"8000"))
ax.autoscale_view()
plt.show()



#for filename in glob.glob(os.path.join('traceblok/velkehadzanie/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
#    if "_" not  in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
#         if "_" not in filename:   
#            
#            nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
#            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
#            if otacky==5:
#                z =abs(df[df['nazov']==nazov]['daleko'].item()-df[df['nazov']==nazov]['blizko'].item())
#                print(z)
#                while z in l_z:
#                    z+=0.8
#                l_z.append(z)
 #               print(filename)
 #               
 #               prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
 #               x,y = furier(prud, t,500)
 #               ax.plot(x[:], y[:], zs=z, zdir='y', alpha=1)
 #               #ax.plot(x, y, zs=z, zdir='y', alpha=0.8)
       
# =============================================================================
# for filename in glob.glob(os.path.join('traceblok/malehadzanie', '*.ST1')): #načíta všetky súbory zo zložky traceblok
#     if "_" not in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
#         #print(filename)
#         nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
#         otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
#         if otacky==5:
#             print(nazov)
#             z = df[df['nazov']==nazov]['blizko']
#             prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
#             x,y = furier(prud, t,50)
#             ax.plot(x[50:], y[50:], zs=z, zdir='y', alpha=0.8)
#             #ax.plot(x, y, zs=z, zdir='y', alpha=0.8)
#             z+=1
#             #plt.figure()
#             #plt.plot(x,y)            
#  
#            
# =============================================================================
            

#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#mplcursors.cursor().connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
#plt.show()


