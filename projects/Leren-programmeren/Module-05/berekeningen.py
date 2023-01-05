def addition(number1: float, number2: float):
    return f"{number1} + {number2} = {float(number1) + float(number2)}"

def subtraction(number1: float, number2: float):
    return f"{number1} - {number2} = {float(number1) - float(number2)}"

def multiplication(number1: float, number2: float):
    return f"{number1} x {number2} = {float(number1) * float(number2)}"

def division(number1: float, number2: float):
    return f"{number1} / {number2} = {float(number1) / float(number2)}"

choice = input("""wat wilt u doen?
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getal ophogen
F) getal verlagen
G) getal verdubbelen
H) getal halveren
Kies: """).upper()


if choice == "A":
    answer = addition(input("Getal een: "), input("Getal twee: "))
    print(answer)
elif choice == "B":
    answer = subtraction(input("Getal een: "), input("Getal twee: "))
    print(answer)
elif choice == "C":
    answer = multiplication(input("Getal een: "), input("Getal twee: "))
    print(answer)
elif choice == "D":
    answer = division(input("Getal een: "), input("Getal twee: "))
    print(answer)
elif choice == "E":
    answer = addition(input("Getal: "), 1)
    print(answer)
elif choice == "F":
    answer = subtraction(input("Getal: "), 1)
    print(answer)
elif choice == "G":
    answer = multiplication(input("Getal: "), 2)
    print(answer)
elif choice == "H":
    answer = division(input("Getal: "), 2)
    print(answer)
else:
    print("that's not a option")
    