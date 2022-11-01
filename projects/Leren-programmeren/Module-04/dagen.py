week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


for i in range(0, 7):
    print(f"alle dagen: {week[i]}")

print("\n")
for i in range(0, 5):
    print(f"alle werkdagen: {week[i]}")

print("\n")
for i in range(5, 7):
    print(f"weekend: {week[i]}")

print("\n")
for i in range(6, -1, -1):
    print(f"alle dagen omgekeerd: {week[i]}")

print("\n")
for i in range(4, -1, -1):
    print(f"werkdagen omgekeerd: {week[i]}")

print("\n")
for i in range(6, 4, -1):
    print(f"weekend omgekeerd:  {week[i]}")
