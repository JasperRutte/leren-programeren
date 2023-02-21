from functions import *

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")

bestelling = True

while bestelling:
    userInput = intInput("Hoeveel bolletjes wilt u? ")

    if userInput > 8:
        print("Zulke grote bakjes hebben wij niet")
        continue
    elif userInput <= 0:
        print("Dat zijn te weinig bolletjes")
        continue
    else:
        if userInput <= 3:
            bakjeHoorntje = askUser("Wilt u een bakje of een hoorntje? ", ["bakje", "hoorntje"])
        else:
            bakjeHoorntje = "bakje"
            print(f"Dan krijgt u van mij een {bakjeHoorntje} met {userInput} bolletjes")

    print(f"Hier is uw {bakjeHoorntje} met {userInput} bolletjes")
    again = askUser("Wilt u nog  een keer bestellen? (J/N): ", ["j", "n"])

    if again == "n":
        bestelling = False

print("tot ziens!")