#Aare Toomist
#02.04.2021
#Harjutus:Täringud

from random import randint # impordin suvaliste arvude kasutamise


taringute_arv = int(input("Sisesta täringute arv: "))#Sisestan täringute arvu
suvaline_taisarv = randint(1,6)# määran suvaliste arvude vahemiku
i = 1 # määran muutuja kordajaks 1

while i <= taringute_arv:# while tsükkel
    print(randint(1,6)) #prindin suvalise arvu 1-6
    i += 1 # lõpetan tsükli

