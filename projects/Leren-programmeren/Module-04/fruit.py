from fruitmand import fruitmand
import random
import math

# opdracht 1
# print(fruitmand)

# opdracht 2
# print(len(fruitmand))

# opdracht 3
# for i in range(0,len(fruitmand)):
#     print(fruitmand[i]['name'])

# opdracht 4
# user_input = int(input("Hoeveel: "))
# random_fruit = random.randint(0, 6)
#
# for i in range(0, user_input):
#     print(fruitmand[random_fruit]['name'])

# opdracht 5
a = len(fruitmand) - 1
for i in range((a), -1, -1):
    print(fruitmand[i]['name'])

# opdracht 6
# print(fruitmand[1]['weight'])

# opdracht 7
# for fruit in fruitmand:
#   if fruit["round"]:
#     print(fruit["name"])

# opdracht 8
# a = 0
# fruitmand.append({'name': 'watermeloen', 'weight': 2000, 'color': 'green', 'round': True})
#
# for i in fruitmand:
#   b = fruitmand[i]['weight']
#   a += b
# print(a)

# opdracht 9
# fruitmand.pop(4)
# for i in fruitmand:
#   print(fruitmand[i]['color'])

# opdracht 10
# a = sorted(fruitmand, key=lambda i: i['weight'])
# for i in a:
#     print(f'{i["name"]}: {i["weight"]}')
