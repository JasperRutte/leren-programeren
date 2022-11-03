import random

colors = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
amount = [0, 0, 0, 0, 0]
results = {}

userinput = int(input("Hoeveel: "))

for i in range(0, userinput):
    a = random.randint(0, 4)
    amount[a] += 1
    results.update({colors[a]: amount[a]})

print(results)
