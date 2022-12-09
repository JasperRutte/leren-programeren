def tafels(cijfer: int):
    for i in range(1, 11):
        print(f"{i} x {cijfer} = {i * cijfer}")


tafels(int(input("Van welk getal wilt u de tafel zien?: ")))
