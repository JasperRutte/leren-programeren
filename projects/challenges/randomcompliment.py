import random

naam = input("naam: ")
number = int(input("nummer: "))
COMPLIMENTS = ("Je bent geweldig ", "Je bent episch ", "Je bent amazing ", "Je bent knap ", "Je bent slim ")
randomNum = random.randint(0, 5)

for i in range(number):
    print(COMPLIMENTS[randomNum] + naam)