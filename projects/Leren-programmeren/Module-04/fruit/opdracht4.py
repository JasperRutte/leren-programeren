from fruitmandplus import fruitmand
import random
a = -1
user_input = int(input("Hoeveel: "))

for i in fruitmand:
    a += 1


for i in range(0, user_input):
    random_fruit = random.randint(0, a)
    print(fruitmand[random_fruit]['name'])