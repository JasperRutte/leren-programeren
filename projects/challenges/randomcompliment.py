import random

naam = input("naam: ")
number = int(input("nummer: "))
COMPLIMENTS = ("Je bent geweldig ", "Je bent episch ", "Je bent amazing ", "Je bent knap ", "Je bent slim ")
aids = 0
for i in range(number):
    randomNum = random.randint(0, 4)
    while aids == randomNum:
        randomNum = random.randint(0, 4)
    print(COMPLIMENTS[randomNum] + naam)
    aids = randomNum

