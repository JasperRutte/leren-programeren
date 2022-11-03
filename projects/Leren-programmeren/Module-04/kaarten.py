import random

SOORT = ("harten ", "klaveren ", "schoppen ", "ruiten ")
NUMMERS_PLAATJES = ("aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer")
deck = ["joker", "joker"]

for a in SOORT:
    for b in NUMMERS_PLAATJES:
        ab = a + b
        deck.append(ab)

random.shuffle(deck)

for i in range(1,8):
    print(f"kaar {i}: {deck[i]}")
    deck.pop(i)

print(f"aantal kaarten: {len(deck)} {deck}")