import matplotlib.pyplot as plt
from spracovanie import *
import glob
import os
import numpy as np
plt.close('all')
datam=[]
data1m=[]
data2m=[]
data3m=[]
data=[]
data2=[]
data3=[]

podmienka1="4"
df = pd.read_csv('hadzanie.csv', header = 0)
hodiny_stav = pd.read_csv('hodiny_stav.csv', header = 0)

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
l_z=[]

for filename in glob.glob(os.path.join('traceblok/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
    if "_" not  in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
         if "4" in filename:   
            
            nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
            if otacky==5:
                #z =hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item()
                z =abs(df[df['nazov']==nazov]['daleko'].item()+df[df['nazov']==nazov]['blizko'].item())
                #z =abs(df[df['nazov']==nazov]['predok'].item())
                print(z)
                #while z in l_z:
                    #z+=0.2
                l_z.append(z)
                print(filename)
                
                prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
                y,x = furier2(prud, t,500)
                #ax.plot(x[0], y[0], zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                datam.append(filename.split("\\")[-1].split(".")[0]) 
                data.append(subor_priemer(filename.split("\\")[-1].split(".")[0]))
                #ax.plot(x, y, zs=z, zdir='y', alpha=0.8)
                  
            
fig, ax = plt.subplots()
ind = np.arange(len(data))
width = 0.2

plt.bar(l_z, data, width=width, bottom=None)
#plt.bar(ind + width, data2, width, bottom=0)
#plt.bar(ind + 2*width, data3, width, bottom=0)

ax.set_title('Prúd pri 5000 v závislosti od hádzania')
#ax.set_xticks(ind + width / 2)
#ax.set_xticklabels([x[:3] for x in datam])
plt.xlabel("hádzanie")
plt.ylabel("Prúd [A]")
#ax.legend((p1[0]), ('3000'))
ax.autoscale_view()
plt.show()
 