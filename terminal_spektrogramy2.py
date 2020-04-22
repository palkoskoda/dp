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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
l_z=[]

for filename in glob.glob(os.path.join('traceblok/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
    if "_" not  in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
         if "X" not in filename:   
            
            nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
            if otacky==5:
                z =hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item()
                #z =abs(df[df['nazov']==nazov]['daleko'].item()-df[df['nazov']==nazov]['blizko'].item())
                #z =abs(df[df['nazov']==nazov]['predok'].item())
                print(z)
                while z in l_z:
                    z+=0.2
                l_z.append(z)
                print(filename)
                
                prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
                y,x = furier2(prud, t,500)
                ax.plot(x[0], y[0], zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                #ax.plot(x, y, zs=z, zdir='y', alpha=0.8)
                
           
            
#z+=10       

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
#ax.set_zscale('log')
#plt.yscale("log")
mplcursors.cursor().connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
plt.show()


