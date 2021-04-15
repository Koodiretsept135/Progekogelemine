#Aare Toomist
#02.04.2021
#Harjutus:Bussid

import math # Matemaatika tehete sisse toomine

Inimeste_arv = int(input("Sisesta inimeste arv: ")) #Inimeste arvu sisestamine
Kohtade_arv = int(input("Sisesta kohtade arv bussis: ")) #Kohtade arvu sisestamine
Busse_vaja = round(Inimeste_arv/Kohtade_arv) # Busside arvutamine kohtade arvu ja inimeste arvu järgi
Viimase_bussi_inimeste_arv = Kohtade_arv * Busse_vaja - Inimeste_arv
Viimane_buss = Busse_vaja + 1

if (Busse_vaja >= 0): #if tingimuslause, kui inimesed mahuvad täpselt bussidesse, kohti üle ei jää
    print("Busse on vaja: " + str(Busse_vaja))
else:
    print("Busse on vaja: " + str(Viimane_buss))
print("Viimases bussis on: " + str(Viimase_bussi_inimeste_arv) + " " + "inimest")
