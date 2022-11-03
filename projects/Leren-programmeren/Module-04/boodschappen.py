boodschappen = {}
userinput = input("wilt u iets toevoegen?(j/n): ").lower()

while userinput == "j":
    grocery = input("Wat wilt u toevoegen: ").capitalize()
    amount = int(input("Hoeveel wilt u er van toevoegen: "))
    if grocery in boodschappen:
        boodschappen[grocery] += amount
    else:
        boodschappen[grocery] = amount
    userinput = input("wilt u iets toevoegen?(j/n): ").lower()

print(f'-[ BOODSCHAPPENLIJSTJE ]-\n')
for grocery in boodschappen:
    amountString = str(boodschappen[grocery])
    print(f"{amountString:>4}x {grocery}")
print(f'\n-------------------------')