kleur_kaas = input("Welke kleur is de kaas: ")
if kleur_kaas == "geel":
    gaten_kaas = input("Zitten er gaten in? ")
    if gaten_kaas == "ja":
        duur_kaas = input("Is de kaas belachelijk duur? ")
        if duur_kaas == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        harde_kaas = input("Is de kaas hard als steen? ")
        if harde_kaas == "ja":
            print("Parmigiano Reggiano")
        else:
            print("Goudsee Kaas")
else:
    blauwe_schimmel = input("Heeft de kaas blauwe schimmel? ")
    if blauwe_schimmel == "ja":
        harde_korst = input("Heeft de kaas een harde korst? ")
        if harde_korst == "ja":
            print("Blue de Rochbaron ")
        else:
            print("foume d'Ambert ")
    else:
        korst = input("Heeft de kaas een korst? ")
        if korst == "ja":
            print("Camembert")
        else:
            print("mozzarella")

