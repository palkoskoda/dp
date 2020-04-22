import matplotlib.pyplot as plt
from spracovanie import *
plt.close('all')

hlavicka(0,0)

vypis_subor("10D3000") #zobrazí zadaný súbor
vypis_subor("42C30") #zobrazí zadaný súbor
vypis_subor("43D3000") #zobrazí zadaný súbor
vypis_subor("44C30") #zobrazí zadaný súbor

pata("zly namer 3000")
hlavicka(3,101)

vypis_subor("10D3000") #zobrazí zadaný súbor
vypis_subor("42C30") #zobrazí zadaný súbor
vypis_subor("43D3000") #zobrazí zadaný súbor
vypis_subor("44C30") #zobrazí zadaný súbor

pata("zly namer 3000")

hlavicka(3,101)

vypis_subor("10D5000") #zobrazí zadaný súbor
vypis_subor("42C50") #zobrazí zadaný súbor
vypis_subor("43D5000") #zobrazí zadaný súbor
vypis_subor("44C50") #zobrazí zadaný súbor

pata("zly namer 5000")

hlavicka(3,101)

vypis_subor("10D8000") #zobrazí zadaný súbor
vypis_subor("42C80") #zobrazí zadaný súbor
vypis_subor("43D8000") #zobrazí zadaný súbor
vypis_subor("44C80") #zobrazí zadaný súbor

pata("zly namer 8000")

hlavicka(3,101)

vypis_subor("41D3000T") #zobrazí zadaný súbor
vypis_subor("41D3000") #zobrazí zadaný súbor
vypis_subor("42D3000") #zobrazí zadaný súbor
vypis_subor("10E30") #zobrazí zadaný súbor
vypis_subor("44D3000") #zobrazí zadaný súbor
vypis_subor("80B3000") #zobrazí zadaný súbor
pata("dobry namer 3000")
hlavicka(3,101)

vypis_subor("41D5000") #zobrazí zadaný súbor
vypis_subor("42D5000") #zobrazí zadaný súbor
vypis_subor("10E50") #zobrazí zadaný súbor
vypis_subor("44D5000") #zobrazí zadaný súbor
vypis_subor("80B5000") #zobrazí zadaný súbor

pata("dobry namer 5000")
hlavicka(3,101)

vypis_subor("41D8000") #zobrazí zadaný súbor
vypis_subor("42D8000") #zobrazí zadaný súbor
vypis_subor("10E80") #zobrazí zadaný súbor
vypis_subor("44D8000") #zobrazí zadaný súbor
vypis_subor("80B8000") #zobrazí zadaný súbor

pata("dobry namer 8000")
hlavicka(3,101)

vypis_subor("80D3000") #zobrazí zadaný súbor
vypis_subor("10A3000") #zobrazí zadaný súbor
vypis_subor("10B3000") #zobrazí zadaný súbor
vypis_subor("80C3000") #zobrazí zadaný súbor
vypis_subor("44C30") #zobrazí zadaný súbor

pata("nove 3000")
hlavicka(3,101)

vypis_subor("80D5000") #zobrazí zadaný súbor
vypis_subor("10A5000") #zobrazí zadaný súbor
vypis_subor("10B5000") #zobrazí zadaný súbor
vypis_subor("80C5000") #zobrazí zadaný súbor
vypis_subor("44C50") #zobrazí zadaný súbor

pata("nove 5000")
hlavicka(3,101)

vypis_subor("80D8000") #zobrazí zadaný súbor
vypis_subor("10A8000") #zobrazí zadaný súbor
vypis_subor("10B8000") #zobrazí zadaný súbor
vypis_subor("80C8000") #zobrazí zadaný súbor
vypis_subor("44C80") #zobrazí zadaný súbor

pata("nove 8000")



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