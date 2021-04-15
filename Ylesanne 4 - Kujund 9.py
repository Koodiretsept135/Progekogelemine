#Aare Toomist
#02.04.2021
#Harjutus: Turtle kujund nr. 9

import turtle

turtle.getscreen()

#ekraani seaded
aken = turtle.Screen()
aken.setup(500,500) #x,y
aken.bgcolor("yellow")
aken.title("Koduülesanne 4 - Kujund nr. 9")


def puzzle_element():# tegin puzzle tüki funktsiooni
    
    for i in range(0,1):#tegin for loobi kuni tagasipöördeni paremale
        turtle.fd (50)
        turtle.lt(90)
        turtle.fd (50)
        turtle.rt(90)
        turtle.fd (50)
    turtle.rt(90)# teine tagasipööre paremale
    for i in range(0,1):#edaspidi kordan for loopi ja tagasipööret paremale, kuni jõuan alguspunkti
        turtle.fd (50)
        turtle.lt(90)
        turtle.fd (50)
        turtle.rt(90)
        turtle.fd (50)
    turtle.rt(90)
    for i in range(0,1):
        turtle.fd (50)
        turtle.lt(90)
        turtle.fd (50)
        turtle.rt(90)
        turtle.fd (50)
    turtle.rt(90)
    for i in range(0,1):
        turtle.fd (50)
        turtle.lt(90)
        turtle.fd (50)
        turtle.rt(90)
        turtle.fd (50)
        
puzzle_element()#prindin puzzle_elemendi funktsiooni 4 korda
puzzle_element()
puzzle_element()
puzzle_element()