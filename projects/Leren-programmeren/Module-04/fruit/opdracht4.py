from fruitmand import fruitmand
import random

user_input = int(input("Hoeveel: "))
random_fruit = random.randint(0, 6)

for i in range(0, user_input):
    print(fruitmand[random_fruit]['name'])