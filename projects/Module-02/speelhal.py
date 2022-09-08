aantal_personen = float(input("Hoeveel personen zijn er? "))
aantal_minuten = float(input("Hoeveel minuten wilt u VR spelen? "))

toegangticket = 7.45 * aantal_personen
vipkaart = 0.37 * aantal_minuten * aantal_personen
totaal = toegangticket + vipkaart
print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {aantal_minuten} minuten VR kost je maar {totaal} euro')