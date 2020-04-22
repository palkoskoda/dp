import matplotlib.pyplot as plt
from spracovanie import *
plt.close('all')
from mpl_toolkits.mplot3d import Axes3D
import glob
import os

#plt.figure()
#prud, t =subor_prud("30B_T2_1")
#x,y = furier(prud, t,50)
#plt.plot(x,y)



☺fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z=0
for filename in glob.glob(os.path.join('traceblok/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
    if "_" not in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
        if "4" in filename :
  
            nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
            otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
            if otacky==5:
                #z =hodiny_stav[hodiny_stav["nazov"]==nazov]["hodiny"].item()
                z =abs(df[df['nazov']==nazov]['daleko'].item()-df[df['nazov']==nazov]['blizko'].item())
                #z =abs(df[df['nazov']==nazov]['predok'].item())
                print(z)
                while z in l_z:
                    z+=0.2
                l_z.append(z)
                print(filename)
                
                prud, t =subor_prud(filename.split("\\")[-1].split(".")[0])
                y, x = furier2(prud, t,500)
                ax.plot(x[1:], y[1:], zs=z, zdir='y', alpha=1, label=filename.split("\\")[-1].split(".")[0])
                #ax.plot(x, y, zs=z, zdir='y', alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#plt.yscale("log")
plt.show()