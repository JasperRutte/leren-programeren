import random

for rondes in range(1, 20):
    randomNumb = random.randint(1,1000)
    for tries in range(1,10):
        userInput = input("Voer een getal tussen 1-1000 in: ")
        if randomNumb == userInput:
            print("correct")
        elif randomNumb < userInput:
            print("wrong! guess bigger")