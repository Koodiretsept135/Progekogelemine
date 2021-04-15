#Aare Toomist
#22.03.2021
#Harjutus - Isiklik alarm



kell_heliseb = int(input("Sisestage mitu korda kell heliseb = "))# Programm kõsib Manivaldilt helinate arvu
helin = 0 #while -tsükli algus muutuja on 0, kuna programmeerimisel on algusväärtus 0

while helin < kell_heliseb:# while tsükkel, mille piirajaks on Manivaldi poolt sisestatud arv
    print("Tõuse ja sära!.") # Äratuskella helinaga kaasnev sõnum
    helin += 1 # while tsükli lõpetamise tingimus
