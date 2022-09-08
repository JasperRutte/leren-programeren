import math
#print("voor 20 pannekoeken heeft u nodig:")
#print(str(500) + "gram bloem")
#print(str(500) + "ml melk")
#print(str(3) + "eieren")
#print(str(1) + "tl zout")
#print(str(30) + "g boter")
#print("eet smakelijk!")


#bloem = 500
#melk = 500
#eieren = 3
#zout = 1
#boter = 30

#print("Voor 20 pannekoeken heeft u nodig:\n" f'{bloem} gram bloem\n{melk} ml melk\n{eieren} eieren\n{zout} tl zout\n{boter} g boter\n\n eet smakeljk!')

hoeveelheid = int(input("hoeveel panekoeken wilt u: "))

bloem = 500/20 * hoeveelheid
melk = 500/20 * hoeveelheid
eieren = 3/20 * hoeveelheid
zout = 1/20 * hoeveelheid
boter = 30/20 * hoeveelheid

print(f'voor {hoeveelheid} panekoeken heb je nodig: \n{bloem} gram bloem\n {melk} L melk\n{math.ceil(eieren)} eieren\n{zout} Tl zout\n{boter} g boter\n\n eet smakelijk!5')
