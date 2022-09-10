hoeveel_crossiants = int(input("Hoeveel crossiants wilt u? "))
hoeveel_stokbroden = int(input("Hoeveel stokbroden wilt u? "))
hoeveel_kortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u? "))

croissant = 0.39 * hoeveel_crossiants
stokbrood = 2.78 * hoeveel_stokbroden
kortingsbon = 1.50 * hoeveel_kortingsbonnen
totaal = croissant + stokbrood - kortingsbon
print(f'De feestlunch kost je bij de bakker {totaal:.2f} euro voor de {hoeveel_crossiants} croissantjes en de {hoeveel_stokbroden} stokbroden als de {hoeveel_kortingsbonnen} kortingsbonnen nog geldig zijn!')

