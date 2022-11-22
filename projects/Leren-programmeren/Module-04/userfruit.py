from fruitmand import fruitmand

askColor = ""
isFound = False
roundTrue = 0
roundFalse = 0


while not isFound:
    askColor = input("kleur? ")
    for i in fruitmand:
        if askColor == i['color']:
            print("test")
            isFound = True
            break
        else:
            print("bestaat niet")


if isFound:
    if roundTrue > roundFalse:
        print(f'Er zijn {roundTrue - roundFalse} meer ronde vruchten dan niet ronde vruchten in de kleur {askColor}')
    elif roundTrue < roundFalse:
        print(f'Er zijn {abs(roundTrue - roundFalse)} minder ronde vruchten dan niet ronde vruchten in de kleur {askColor}')
    elif roundTrue == roundFalse:
        print(f'Er zijn {roundTrue} ronde vruchten en {roundFalse} niet ronde vruchten in de kleur {askColor}')