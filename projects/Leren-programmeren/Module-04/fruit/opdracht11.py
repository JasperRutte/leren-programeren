from fruitmand import fruitmand


isFound = False
roundTrue = 0
roundFalse = 0

while not isFound:
    askColor = input("kleur? ").lower()
    for i in fruitmand:
        if askColor == i['color']:
            if i['round']:
                roundTrue += 1
            else:
                roundFalse += 1
            isFound = True
    if not isFound:
        print(f"De kleur {askColor} zit er niet in de fruitmand")

if roundTrue > roundFalse:
    print(f'Er zijn {roundTrue - roundFalse} meer ronde vruchten dan niet ronde vruchten in de kleur {askColor}')
elif roundTrue < roundFalse:
        print(f'Er zijn {abs(roundTrue - roundFalse)} minder ronde vruchten dan niet ronde vruchten in de kleur {askColor}')
elif roundTrue == roundFalse:
    print(f'Er zijn {roundTrue} ronde vruchten en {roundFalse} niet ronde vruchten in de kleur {askColor}')