from random import shuffle

names = []
amount = len(names)
more_names = False

while amount < 3:
    print(f"voeg minimaal {3 - amount} namen toe")
    add_name = input("Voeg een naam toe: ")
    if add_name in names:
        print("Naam bestaat al\n")
    else:
        names.append(add_name)
        amount = len(names)

while not more_names:
    print("type quit to stop")
    add_name = input("Voeg een naam toe: ")
    if add_name == "quit":
        break
    elif add_name in names:
        print("Naam bestaat al\n")
    else:
        names.append(add_name)

shuffle(names)

person = names[-1]
for people in names:
    print(f"{person} heeft {people} getrokken")
    person = people
