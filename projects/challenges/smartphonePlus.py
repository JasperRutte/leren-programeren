iphone = float(input("Hoeveel kost de Iphone: "))
samsung = float(input("Hoeveel kost de Samsung: "))
asus = float(input("Hoeveel kost de Asus: "))

# bepaling welke telefoon het duurst, middel en goedkoopst is
if iphone > samsung and iphone > asus:
    expensive = str("Iphone")
    expensivePrice = iphone
    if samsung > asus:
        middle = str("Samsung")
        middlePrice = samsung
        cheap = str("Asus")
        cheapPrice = asus
    else:
        middle = str("Asus")
        middlePrice = asus
        cheap = str("Samsung")
        cheapPrice = samsung
elif samsung > iphone and samsung > asus:
    expensive = str("Samsung")
    expensivePrice = samsung
    if iphone > asus:
        middle = str("Iphone")
        middlePrice = iphone
        cheap = str("Asus")
        cheapPrice = asus
    else:
        middle = str("Asus")
        middlePrice = asus
        cheap = str("Iphone")
        cheapPrice = iphone
elif asus > samsung and asus > iphone:
    expensive = str("Asus")
    expensivePrice = asus
    if samsung > iphone:
        middle = str("Samsung")
        middlePrice = samsung
        cheap = str("Iphone")
        cheapPrice = iphone
    else:
        middle = str("Iphone")
        middlePrice = iphone
        cheap = str("Samsung")
        cheapPrice = samsung

print(f"De {expensive} is het duurst, de telefoon kost: {expensivePrice}")
print(f"De {cheap} is het goedkoopst, de telefoon kost: {cheapPrice}")
print(f"De {middle} zit er tussen in met: {middlePrice}")

# Bepaling wat voor advies
verschilAsus = asus - middlePrice
verschilIphone = iphone - middlePrice

if iphone > 900 and samsung > 900 and asus > 900:
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
elif verschilIphone <= 50:
    print(f"Het advies dus de iphone te kopen, deze is namelijk {verschilIphone} goedkoper/duurder dan de {middle}")
else:
    print(f"Het advies is dus de Samsung te kopen, deze is namelijk het goedkoopst")
    # test
