import random

soort = ["harten ", "klaveren ", "schoppen ", "ruiten "]
nummers_plaatjes = ["aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer"]
shuffled = ["joker", "joker"]

for x in range(0,4):
    a = soort[x]
    for y in range(0, 13):
        b = nummers_plaatjes[y]
        ab = a + b
        shuffled.append(ab)

random.shuffle(shuffled)

for i in range(1,6):
    print(f"kaar {i}: {shuffled[i]}")

print(shuffled)