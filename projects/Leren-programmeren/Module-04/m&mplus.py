import random

colors = ("Rood", "Blauw", "Groen", "Geel", "Bruin")
amount = [0, 0, 0, 0, 0]


userinput = int(input("Hoeveel: "))

for i in range(0, userinput):
    a = random.randint(0,4)
    amount[a] += 1

results = {
    colors[0]: amount[0],
    colors[1]: amount[1],
    colors[2]: amount[2],
    colors[3]: amount[3],
    colors[4]: amount[4]
}
print(results)