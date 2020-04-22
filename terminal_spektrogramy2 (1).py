import matplotlib.pyplot as plt
from spracovanie import *
import pandas as pd
plt.close('all')
from mpl_toolkits.mplot3d import Axes3D
import glob
import os
import csv
import mplcursors

podmienka1="4"
df = pd.read_csv('hadzanie.csv', header = 0)
hodiny_stav = pd.read_csv('hodiny_stav.csv', header = 0)

#fig = plt.figure()
plt.rcParams["figure.figsize"] = 12.6, 6.6
#ax = fig.add_subplot(111, projection='3d')
ax = plt.axes( projection='3d')
l_z=[]

spodna_frekvencia=1050
vrchna_frekvencia=0
spodna_frekvencia2=100.5
vrchna_frekvencia2=99.5
okrem_frekvencie=[50,100]

for filename in glob.glob(os.path.join('traceblok/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
    if "_" not  in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
         if "4"  in filename:   

            nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
            if otacky==5:
                #z =hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item()
                z =abs(df[df['nazov']==nazov]['daleko'].item()+2*df[df['nazov']==nazov]['blizko'].item())
                #z =abs(df[df['nazov']==nazov]['blizko'].item())
                
                while z in l_z:
                    z+=0.3
                l_z.append(z)
                print(z)
                print(filename)
                
                prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
                #y,x = furier2(depeakf (prud, t, 300, 2, 10)[0], t,500)
                #ax.plot(x[:], signal.savgol_filter(np.log(y[:]), 51,3), zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                #ax.plot(x[:], np.log(y[:]), zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                y,furier_x=furier2(prud, t,500)
                
                norm_index=int(otacky*400/6)
                norm=y[331]+y[330]+y[329]
                y=y/norm
                #g=[x for ind, x in enumerate(furier_x) if spodna_frekvencia*4 < ind < vrchna_frekvencia*4]
                g=[x for ind, x in enumerate(furier_x) if ((spodna_frekvencia*4/3*otacky > ind  > vrchna_frekvencia*4/3*otacky)and (spodna_frekvencia2*4/3*otacky > ind or ind > vrchna_frekvencia2*4/3*otacky))]
                h=[x for ind, x in enumerate(y) if ((spodna_frekvencia*4/3*otacky > ind  > vrchna_frekvencia*4/3*otacky)and (spodna_frekvencia2*4/3*otacky > ind or ind > vrchna_frekvencia2*4/3*otacky))]
                #h=np.log(h)
                ax.plot(g[:], h[:], zs=z, zdir='y', label=filename.split("\\")[-1].split(".")[0], alpha=0.8)
               


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
            

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
mplcursors.cursor().connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
plt.show()


