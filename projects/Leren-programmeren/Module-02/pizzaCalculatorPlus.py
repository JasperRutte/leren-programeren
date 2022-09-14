smallBedrag = 8
mediumBedrag = 9.5
largeBedrag = 12
print("Large pizza    : 12 euro\nmedium pizzas  : 9,50 euro\nsmall pizzas   : 8 euro\n")  # kosten van alle pizzas


def numberCheck(vraag: str) -> int:  # checkt of vraag een integer is
    try:
        aantal = int(input(vraag))
    except ValueError:
        print("Gebruik alleen HELE getallen!")
        return numberCheck(vraag)
    return aantal


smallPizza = (numberCheck("Hoeveel small pizza's wilt u: "))  # geeft "vraag" een vraag
mediumPizza = (numberCheck("Hoeveel medium pizza's wilt u: "))
largePizza = (numberCheck("Hoeveel large pizza's wilt u: "))

print(
    f'\nUw bestelling:\n{smallPizza}x small pizzas\n{mediumPizza}x medium pizzas\n{largePizza}x large pizzas')  # bon printen
total = smallPizza * smallBedrag + mediumPizza * mediumBedrag + largePizza * largeBedrag  # uitrekenen hoeveel alles bij elkaar kost
print(f'\nTotaal bedrag is {total:.2f} euro.')  # Totaal bedrag uitrekenen
