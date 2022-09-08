#large 12 euro
#medium 9,50 euro
#small 8 euro

def pizzaCalculator():
    print("Large pizza    : 12 euro\nmedium pizzas  : 9,50 euro\nsmall pizzas   : 8 euro") #\n word gebruikt om een line over te slaan in de print
    print("Hoeveel large pizzas wilt u? ")
    largePizzas = int(input())
    print("Hoeveel medium pizzas wilt u? ")
    mediumPizzas = int(input())
    print("Hoeveel small pizzas wilt u? ")
    smallPizzas = int(input())
    print(f'\nUw bestelling:\n{largePizzas}x large pizzas\n{mediumPizzas}x medium pizzas\n{smallPizzas}x small pizzas')#Het bonnetje printen
    total = largePizzas * 12 + mediumPizzas * 9.50 + smallPizzas * 8 #uitrekenen hoeveel alles bij elkaar kost
    print(f'\nTotaal bedrag is {total} euro.')

pizzaCalculator()