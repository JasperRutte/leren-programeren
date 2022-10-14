x = float(input("Lengte: "))
y = float(input("Breedte: "))
z = float(input("Hoogte/Diepte: "))
kubiekeMeter = x * y * z

afstand = int(input("Afstand van het bedrijf: "))

uitgave = kubiekeMeter * 25
afvoerGrond = 32.5 * kubiekeMeter
totaal = afvoerGrond + uitgave

print(f"""
Offerte voor een zwembad van {x} bij {y} bij {z} meter (inhoud:{kubiekeMeter}m3)
Uitgaven: {uitgave}
Afvoeren grond {afvoerGrond}
Totaal: {totaal}""")