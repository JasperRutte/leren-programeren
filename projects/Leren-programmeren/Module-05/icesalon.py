print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")

bestelling = True

while bestelling:
    userInput = input('Hoeveel bolletjes wilt u? ')
    try:
        userInput = int(userInput)
    except ValueError:
        print('Sorry, dit herken ik niet!')
        continue
    if userInput > 8:
        print("Zulke grote bakjes hebben wij niet")
        continue
    elif userInput <= 0:
        print("Dat zijn te weinig bolletjes")
        continue
    else:
        if userInput <= 3:
            bakjeHoorntje = input("Wilt u een bakje of een hoorntje").lower()
            while bakjeHoorntje != "bakje" and bakjeHoorntje != "hoorntje":
                print("Sorry dat snap ik niet")
                bakjeHoorntje = input("Wilt u een bakje of een hoorntje").lower()
        else:
            print(f"Dan krijgt u van mij een bakje met {userInput} bolletjes")
            bakjeHoorntje = "bakje"

    print(f"Hier is uw {bakjeHoorntje} met {userInput} bolletjes")

    again = input("Wilt u nog een keer bestellen? (J/N)").upper()
    while again != "J" and again != "N":
        print("Sorry dat snap ik niet")
        again = input("Wilt u nog een keer bestellen? (J/N)").upper()

    if again == "N":
        print("tot ziens")
        bestelling = False
