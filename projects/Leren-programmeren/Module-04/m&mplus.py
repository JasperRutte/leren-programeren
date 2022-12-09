import random

colors = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
results = {}

userinput = int(input("Hoeveel: "))

for i in range(userinput):
    a = random.randint(0, len(colors)-1)
    if colors[a] not in results:
        results.update({colors[a]: 1})
    else:
        x = results.get(colors[a]) + 1
        results.update({colors[a]: x})

print(results)