import matplotlib.pyplot as plt
import csv

hodiny=[] 
cas_merania=[7128, 9144, 9312, 8496]
data2=[]

podmienka1="4"

with open("vretena hodiny.csv", newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=',', quotechar='\n'))
    for row in data[1:]:#citam od druheho riadku
        a= (int(row[2])-int(row[1]))*8760/cas_merania[0]#casy medzi 1. a 2. stlpcom delim plnym casom medzi meraniami
        if a>0 and row[0][0]==podmienka1 :#and row[0][-2]=="4":#tato podmienka mi vybera rozdiely vacsie ako 0 a este nieco podla nazvu
            data2.append([row[0], a, "1"])
            
        a= (int(row[3])-int(row[2]))*8760/cas_merania[1]
        if a>0 and row[0][0]==podmienka1:# and row[0][-2]=="4":
            data2.append([row[0], a, "2"])
            
        a= (int(row[4])-int(row[3]))*8760/cas_merania[2]
        if a>0 and row[0][0]==podmienka1:# and row[0][-2]=="4":
            data2.append([row[0], a, "3"])
            
        a= (int(row[5])-int(row[4]))*8760/cas_merania[3]
        if a>0 and row[0][0]==podmienka1 :#and row[0][-2]=="4":
            data2.append([row[0], a, "4"])
    
with open('hodiny_prepocitane.csv', mode='w') as hp_file: #dava to aj do csv
    hp = csv.writer(hp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    hp.writerows(data2)
    
with open('hodiny_stav.csv', mode='w') as hp_file: #dava to aj do csv
    hs = csv.writer(hp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    hs.writerow(["nazov",  "hodiny"])
    for row in data[1:]:
        hs.writerow([row[0],  row[5]])



plt.hist([x[1] for x in data2], bins=range(1000, 7000, 200) )  # od 1000 do 7000 po 200
plt.title("Histogram motohodín za rok")
plt.show()
