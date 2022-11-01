import random

rounds = 0
tries = 0
userInput = ""
points = 0

while rounds < 20 and userInput != "quit":
    rounds += 1
    print(f"rounds: {rounds}")
    randomNum = random.randint(1, 1000)
    for i in range(1,10):
        print(f"\ntries: {i}")
        userInput = input("enter a whole number between 1-1000: ")
        if userInput == "quit":
            break
        else:
            userInput = int(userInput)

        difference = abs(randomNum - userInput)
        if randomNum == userInput:
            print("correct!")
            points += 1
            break
        elif difference < 20 and randomNum < userInput:
            print("wrong, you're very warm, try smaller")
        elif difference < 20 and randomNum > userInput:
            print("wrong, you're very warm, try bigger")
        elif difference < 50 and randomNum < userInput:
            print("wrong, you're warm, try smaller")
        elif difference < 50 and randomNum > userInput:
            print("wrong, you're warm, try bigger")
        elif randomNum < userInput:
            print("Wrong, try smaller")
        else:
            print("Wrong, try bigger")

print(f"\npoints: {points}")
