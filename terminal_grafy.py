import matplotlib.pyplot as plt
from spracovanie import *
plt.close('all')

hlavicka(0,0)
#vypis_subor("44C5000") #zobrazí zadaný súbor
vypis_subor("SKOK3") #zobrazí zadaný súbor
#vypis_subor("44C_DEACC") #zobrazí zadaný súbor


pata("Odchýlka počas skokovej zmeny polohy")




#vypis_subor("80D_T6_3") #zobrazí zadaný súbor
#pata("3000")
#hlavicka(6,51)
#vypis_subor("80D_T6_5") #zobrazí zadaný súbor
#pata("5000")

#prud, t =subor_prud("30B_T2_1")
#plt.figure(1)         
#plt.subplot(211)
#plt.xlabel("x")
#plt.ylabel("Prúd [A]")
#plt.plot(t, prud)
#plt.subplot(212)
#plt.psd(prud, len(prud), len(t)/30)