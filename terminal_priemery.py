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
data1=[]
data2=[]
data3=[]

#uz su priemery 2, tam to funguje lepsie
for filename in glob.glob(os.path.join('traceblok/', '*.ST1')):
    if "\\4" in filename :  
        if "30" in filename :  
            print("30ky")
            print(filename)
            #data1m.append(filename.split("\\")[-1].split(".")[0]) 
            #data1.append(subor_priemer(filename.split("\\")[-1].split(".")[0]))
        if "50" in filename :
            #print(filename)
            data2m.append(filename.split("\\")[-1].split(".")[0]) 
            data2.append(subor_priemer(filename.split("\\")[-1].split(".")[0]))
        if "80." in filename :
            print("80ky")
            print(filename)
            data1m.append(filename.split("\\")[-1].split(".")[0]) 
            data1.append(subor_priemer(filename.split("\\")[-1].split(".")[0]))    
        if "800" in filename :
            print("80ky")
            print(filename)
            data1m.append(filename.split("\\")[-1].split(".")[0]) 
            data1.append(subor_priemer(filename.split("\\")[-1].split(".")[0]))    
     
          
print(data1)
print(data3)            
fig, ax = plt.subplots()
ind = np.arange(len(data1))
width = 0.25
plt.bar(ind, data1, width, bottom=0)
plt.bar(ind + width, data2, width, bottom=0)
plt.bar(ind + 2*width, data3, width, bottom=0)

ax.set_title('Prúd v závislosti od otáčok')
#ax.set_xticks(ind + width / 2)
ax.set_xticklabels([x[:3] for x in data1m])

ax.legend((p1[0], p2[0], p3[0]), ('3000', '5000',"8000"))
ax.autoscale_view()
plt.show()
 