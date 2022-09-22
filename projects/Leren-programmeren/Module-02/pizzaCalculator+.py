def vraagNaarAantal(vraag: str) -> int: # vraagNaarAantal() is een functie die een vraag stelt en een int teruggeeft
    """Vraag naar een aantal en geef het aantal terug."""
    try:
        aantal = int(input(vraag)) # vraag naar een aantal
    except ValueError: # als de gebruiker geen int invoert geef een foutmelding
        print("Geef een getal in.") # geef een foutmelding
        return vraagNaarAantal(vraag) # vraag opnieuw naar een aantal
    return aantal # geef het aantal terug

print(vraagNaarAantal("Hoeveel large pizza's wil je? "))
print(vraagNaarAantal("Hoeveel medium pizza's wil je? "))
print(vraagNaarAantal("Hoeveel small pizza's wil je? "))















# large 12 euro
# medium 9,50 euro
# small 8 euro

# def vraagNaarAantal(vraag: str) -> int:
#        aantal = int(input("hoeveel small pizza's? "))
#
#        return aantal

# largePizza = int(input("Hoeveel large pizza's wilt u: "))
# mediumPizza = int(input("Hoeveel medium pizza's wilt u: "))
# smallPizza = int(input("Hoeveel medium pizza's wilt u: "))

# smallPizza = vraagNaarAantal("Hoeveel small pizza's? 1111111111111")
# print(smallPizza)



# def pizzaCalculator():
#     print("Large pizza    : 12 euro\nmedium pizzas  : 9,50 euro\nsmall pizzas   : 8 euro") # \n word gebruikt om een line over te slaan in de print
#     print("Hoeveel large pizzas wilt u? ")
#     try:
#         largePizzas = int(input())
#     except ValueError:
#         print("je kan geen decimale getallen invullen")
#     finally:
#         print("test")
#     print("Hoeveel medium pizzas wilt u? ")
#     mediumPizzas = int(input())
#     print("Hoeveel small pizzas wilt u? ")
#     smallPizzas = int(input())
#     print(f'\nUw bestelling:\n{largePizzas}x large pizzas\n{mediumPizzas}x medium pizzas\n{smallPizzas}x small pizzas')# Het bonnetje printen
#     total = largePizzas * 12 + mediumPizzas * 9.50 + smallPizzas * 8 # uitrekenen hoeveel alles bij elkaar kost
#     print(f'\nTotaal bedrag is {total} euro.')

# pizzaCalculator()

