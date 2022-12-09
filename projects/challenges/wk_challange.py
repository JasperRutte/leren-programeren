groep_a = []

for x in range(1, 4):
    points = {}
    points.update({input(f"land {x}: "): 0})
    groep_a.append(points)


for wedstrijden in range(0, 3):
    print(f"wedstrijd {wedstrijden}")
    print(f"{groep_a[0]} tegen {groep_a[1]} ")

