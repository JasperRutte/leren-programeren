iphone = float(input("Hoeveel kost de iphone? "))
samsung = float(input("Hoeveel kost de Samsung? "))
asus = float(input("Hoeveel kost de Asus: "))
prijsVerschil = iphone - samsung
verschilAsusIphone = asus -
verschilAsusSamsung =

if asus <

elif iphone >= 900 and 900 <= samsung < iphone:
    print(f"De Iphone is het duurst, de telefoon kost: {iphone} euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung} euro")
    print("Het advies is om geen telefoon te kopen, ze zijn te duur.")

elif 900 <= iphone < samsung and samsung >= 900:
    print(f"De Samsung is het duurst, de telefoon kost: {samsung} euro")
    print(f"De Iphone is het goedkoopst, de telefoon kost: {iphone} euro")
    print("Het advies is om geen telefoon te kopen, ze zijn te duur.")

elif prijsVerschil <= 50 and iphone > samsung:
    print(f"De Iphone is het duurst, de telefoon kost: {iphone} euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung} euro")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone")

elif prijsVerschil <= 50 and iphone < samsung:
    print(f"De Samsung is het duurst, de telefoon kost: {samsung} euro.")
    print(f"De Iphone is het goedkoopst, de telefoon kost: {iphone} euro.")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone.")

elif iphone > samsung:
    print(f"De Iphone is het duurst, de telefoon kost: {iphone} euro.")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung} euro.")
    print(f"Het advies is dus de samsung te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone.")

elif iphone < samsung:
    print(f"De Samsung is het duurst, de telefoon kost: {samsung} euro.")
    print(f"De Iphone is het goedkoopst, de telefoon kost: {iphone} euro.")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone.")

else:
    print(f"De telefoon kosten allebei {iphone}.")
    print("Het advies is dus om de Iphone te kopen.")