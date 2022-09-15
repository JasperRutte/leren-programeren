print("\nWelkom bij de vragen lijst. Vul alle ja/nee vragen in met J/j of N/n\n")

dieren_dressuur = int(input("Hoeveel jaar praktijk ervaring heeft u in dieren dressuur?: "))
jongleren = int(input("Hoeveel jaar ervaring heeft u in jongleren?: "))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u in acrobatiek?: "))
diploma = input("Heeft u een MBO-4 diploma op zak?(J/N): ").upper()
vrachtwagen = input("Heeft u een geldig vrachtwagen rijbewijs?(J/N): ").upper()
hoge_hoed = input("Heeft u een hoge hoed?(J/N): ").upper()
snor = int(input("Hoe breed is uw snor?(cm): "))
if snor > 20:
    raise Exception("Big moustache man")
haar = int(input("Hoe lang is uw roodharig krulhaar?(cm): "))
lengte = int(input("Hoe lang bent u?(cm): "))
if lengte < 150:
    raise Exception("midget moment")
gewicht = int(input("Hoeveel weegt u?(kg): "))
certificaat = input("Heeft u een certificaat 'overleven met gevaarlijk personeel'?(J/N): ").upper()
schaal = input("Op een schaal van stoel tot olifant wat is uw favoriete kleur van het alfabet?: ")  # Er hoeft niks gedaan te worden met deze variabel
papier = input("Heeft u wel een papier gegeten?(J/N): ")  # Er hoeft niks gedaan te worden met deze variabel
water = input("Heeft u wel eens eerder water gedronken?(J/N): ")  # Er hoeft niks gedaan te worden met deze variabel
zuurstof = input("Ademt u zuurstof?(J/N): ")  # Er hoeft niks gedaan te worden met deze variabel
if zuurstof == "N":
    raise Exception("Hoe leef je op dit punt nog???")

ervaring = False
if dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3:
    ervaring = True

snor_haar = False
if snor >= 10 or haar >= 20:
    snor_haar = True


if ervaring == True and diploma == "J" and vrachtwagen == "J" and hoge_hoed == "J" and snor_haar == True and lengte >= 150 and gewicht >= 90 and certificaat == "J":
    print("U bent aangenomen!")
else:
    print("U bent niet aangenomen!")
