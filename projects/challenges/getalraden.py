import random

low = 1
high = 1000

while high != low:
    number = random.randint(low, high)
    userInput = int(input(f'Is het getal {number} h/l/g? ')).lower()

    if userInput == 'h':
        low = number
    elif userInput == 'l':
        high = number
    elif userInput == 'g':
        print(f'Dan heb ik het getal geraden, het is {number}')
        break