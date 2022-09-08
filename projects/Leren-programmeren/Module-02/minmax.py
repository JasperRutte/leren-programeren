a = int(input("Noem getal A: "))
b = int(input("Noem getal B: "))

if a > b:
    max = a
    min = b
    print("\nHet maximum is", max)
    print("Het minimum is", min)
elif a < b:
    max = b
    min = a
    print("\nHet maximum is", max)
    print("Het minimum is", min)
else:
    print("\na en b zijn even groot")