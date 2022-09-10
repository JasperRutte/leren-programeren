# ervaring = input("Heeft u praktijkervaring met dieren-dressuur OF ervaring met jongleren OF praktijkervaring met acrobatiek?(J/N): ")
dieren_dressuur = int(input("Hoeveel jaar praktijk ervaring heeft u in dieren dressuur?: "))
jongleren = int(input("Hoeveel jaar ervaring heeft u in jongleren?: "))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u in acrobatiek?: "))
diploma = input("Heeft u een MBO-4 diploma op zak?(J/N): ")
vrachtwagen = input("Heeft u een geldig vrachtwagen rijbewijs?(J/N): ")
hoge_hoed = input("Heeft u een hoge hoed?(J/N): ")
snor = int(input("Hoe breed is uw snor?(cm): "))
haar = int(input("Hoe lang is uw roodharig krulhaar?(cm): "))
lengte = int(input("Hoe lang bent u?(cm): "))
gewicht = int(input("Hoeveel weegt u?(kg): "))
certificaat = input("Heeft u een certificaat 'overleven met vevaarlijk personeel'?(J/N): ")
efteling = input("Hoe vaak bent u bij de Efteling geweest?: ")  #Er hoeft niks gedaan te worden met deze variabel
papier = input("Heeft u wel een papier gegeten?(J/N): ")  #Er hoeft niks gedaan te worden met deze variabel
water = input("Heeft u wel eens eerder water gedronken?(J/N): ")  #Er hoeft niks gedaan te worden met deze variabel
zuurstof = input("Ademt u zuurstof?(J/N): ")  #Er hoeft niks gedaan te worden met deze variabel

ervaring = dieren_dressuur + jongleren + acrobatiek
if dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3:
    ervaring = True

if ervaring == True and diploma == "J" and vrachtwagen == "J" and hoge_hoed == "J" and snor >= 10 and haar >= 20 and lengte >= 150 and gewicht >= 90 and certificaat == "J":
    print("U bent aangenomen!")











# if ervaring == "J":
#     if ervaring == "dieren-dressuur":
#         int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: "))
#         if ervaring >= 4:
#             ervaring = True
#         else:
#             ervaring = False
#     elif ervaring == "jongleren":
#         int(input("Hoeveel jaar praktijkervaring heeft u met jongleren?: "))
#         if ervaring >= 5:
#             ervaring = True
#         else:
#             ervaring = False    
#     elif ervaring == "acrobatiek":
#         int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?: "))
#         if ervaring >= 3:
#             ervaring = True
#         else:
#             ervaring = False
#     else:
#         ervaring = False
# else:
#     ervaring = False

# if diploma == "J":
#     diploma = True
# else:
#     diploma = False

# if vrachtwagen == "J":
#     vrachtwagen = True
# else:
#     vrachtwagen = False

# if hoge_hoed == "J":    
#     hoge_hoed = True
# else:
#     hoge_hoed = False

# if gender == "M":
#     snor = int(input("Hoe breed is uw snor?(antwoord in cm): "))
#     if snor >= 10:
#         snor = True
#         gender = snor
#     else:
#         snor = False
#         gender = snor   
# elif gender == "V":
#     rood_haar = int(input("Hoe lang is uw haar: "))
#     if rood_haar >= 20:
#         rood_haar = True
#         gender = rood_haar
#     else:
#         rood_haar = False
#         gender = rood_haar
# else:
#     snor = False
#     rood_haar = 

