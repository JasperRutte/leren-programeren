iphone = float(input("Hoeveel kost de iphone? "))
samsung = float(input("Hoeveel kost de Samsung? "))
prijsVerschil = iphone - samsung

if prijsVerschil <= 50 and iphone > samsung:
    print(f"De Iphone is het duurst, de telefoon kost: {iphone}")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung}")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone")

elif prijsVerschil <= 50 and iphone < samsung:
    print(f"De Samsung is het duurst, de telefoon kost: {samsung}.")
    print(f"De Iphone is het goedkoopst, de telefoon kost: {iphone}.")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone.")

elif iphone > samsung:
    print(f"De Iphone is het duurst, de telefoon kost: {iphone}.")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung}.")
    print(f"Het advies is dus de samsung te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone.")

elif iphone < samsung:
    print(f"De Samsung is het duurst, de telefoon kost: {samsung}.")
    print(f"De Iphone is het goedkoopst, de telefoon kost: {iphone}.")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {prijsVerschil} euro duurder/goedkoper dan de Iphone.")

else:
    print(f"De telefoon kosten allebei {iphone}.")
    print("Het advies is dus om de Iphone te kopen.")

# if iphone > samsung:
#     print(f"De Iphone is het duurst, de telefoon kost: {iphone}")
#     print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung}")
#     print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {prijsVerschil} euro goedkoper dan de Iphone")
