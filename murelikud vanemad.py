#Aare Toomist
#02.04.2021
#Harjutus:Murelikud vanemad


ringide_arv = int(input("Sisesta ringide arv: "))#Sisestame jooksuringide arvu
ring = 2
porgandid1 = ringide_arv
porgandid2 = ringide_arv + 2
porgandite_summa = porgandid1 + porgandid2

while ring <= ringide_arv:
        print("Porgandite koguarv on " + str (porgandite_summa))
        ring = ring + 1