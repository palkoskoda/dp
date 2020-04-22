import matplotlib.pyplot as plt
from spracovanie import *
import glob
import os
import pandas as pd
import numpy as np

#odoberaný prúd jednotlivých strojov v závislosti od otáčok

plt.close('all')
data= pd.DataFrame(columns=['nazov', 'otacky', 'prud'])


for filename in glob.glob(os.path.join('traceblok/malehadzanie/', '*.ST1')): #načíta všetky súbory zo zložky traceblok
    if "_" in filename :  # ak nájde v názve súboru "_", spracuvava to inak, ako zvysne (stary sposob merania, trash?)
        #print(filename)
        nazov=filename.split("\\")[-1].split(".")[0][0:3] #z nazvu ziska prve 3 znaky (oznacenie stroja)
        otacky=int(filename.split(".")[0][-1]) #posledny znak otacky
        prud=subor_priemer(filename.split("\\")[-1].split(".")[0])#nazov pre funkciu ktora vyrata priemery
        #data=data.append({'nazov': nazov, 'otacky': otacky, 'prud': prud}, ignore_index=True)

        
    else:  #tu su len najnovsie merania, ktore som meral poriadne
        #print(filename)
        nazov=filename.split("\\")[-1].split(".")[0][0:3]
        otacky=int(filename.split("\\")[-1].split(".")[0][3:4])
        prud=subor_priemer(filename.split("\\")[-1].split(".")[0])
        data=data.append({'nazov': nazov, 'otacky': otacky, 'prud': prud}, ignore_index=True)

data3=data[data['otacky']==3] 
data5=data[data['otacky']==5] 
data8=data[data['otacky']==8] 
dataf = pd.merge(data3, data5.rename(columns={'prud':'prud5'}), on='nazov')
dataf = pd.merge(dataf, data8.rename(columns={'prud':'prud8'}), on='nazov')

print(dataf)    


fig, ax = plt.subplots()
ind = np.arange(len(dataf.index))
width = 0.25
plt.bar(ind, dataf['prud'], width, bottom=0, label='3000ot')
plt.bar(ind + width, dataf['prud5'], width, bottom=0, label='5000ot')
plt.bar(ind + 2*width, dataf['prud8'], width, bottom=0, label='8000ot')
ax.set_title('Prúd v závislosti od otáčok')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(dataf['nazov'])
ax.legend()
ax.autoscale_view()

#mplcursors.cursor(hover=True)

plt.show()
 
 