import matplotlib.pyplot as plt
from spracovanie import *
plt.close('all')
import numpy as np
import math
#hlavicka(0,0)

#vypis_subor("10B_T3_1") #zobrazí zadaný súbor
#vypis_subor("10A1") #zobrazí zadaný súbor
#vypis_subor("10A_T3_1") #zobrazí zadaný súbor
#vypis_subor("10B1") #zobrazí zadaný súbor
#vypis_subor("20A_T1_1") #zobrazí zadaný súbor
#vypis_subor("20B_T1_1") #zobrazí zadaný súbor
#vypis_subor("30A_T2_1") #zobrazí zadaný súbor
#pata("1000")


#hlavicka(6,51)
#vypis_subor("80D_T6_3") #zobrazí zadaný súbor
#pata("3000")
#hlavicka(6,51)
#vypis_subor("80D_T6_5") #zobrazí zadaný súbor
#pata("5000")

prud, t =subor_prud("44A3000")
plt.figure(1)         
plt.subplot(211)
plt.xlabel("x")
plt.ylabel("Prúd [A]")
plt.plot(t, prud)
plt.subplot(212)
plt.psd(prud, len(prud), len(t)/4)