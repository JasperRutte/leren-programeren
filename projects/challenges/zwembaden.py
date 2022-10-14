x = float(input("Lengte: "))
y = float(input("Breedte: "))
z = float(input("Hoogte/Diepte: "))
afstand = int(input("Afstand van het bedrijf (km): "))

kubiekeMeter = x * y * z
uitgraven = kubiekeMeter * 25
afvoerGrond = 32.5 * kubiekeMeter

if afstand < 50 and kubiekeMeter < 20:
    voorrijkosten = afstand * 1.25
    totaal = uitgraven + 100 + voorrijkosten
elif afstand >= 50 and kubiekeMeter < 20:
    voorrijkosten = afstand * 1.15
    totaal = uitgraven + 100 + voorrijkosten
elif afstand < 50 and kubiekeMeter >= 20:
    voorrijkosten = afstand * 2.15
    totaal = uitgraven + 250 + voorrijkosten
else:
    voorrijkosten = afstand * 2.05
    totaal = uitgraven + 250 + voorrijkosten

print(f"""
Offerte voor een zwembad van {x} bij {y} bij {z} meter (inhoud:{kubiekeMeter}m3)
Uitgaven: {uitgraven}
Afvoeren grond: {afvoerGrond}
voorrijkosten {voorrijkosten}
Totaal: {totaal}""")