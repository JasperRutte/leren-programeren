# maak lijst met fibonacci reeks
# geef een getal mee aan de functie
# kijk of het getal in de reeks zit
# ga vanaf dat getal de hoeveelheid geta


def fibo(nummer: int):
    nieuw = 1
    oud = 0
    oud2 = 0
    reeks = []
    for x in range(0, 100):
        reeks.append(oud)
        oud = nieuw
        nieuw += oud2
        oud2 = oud

    if nummer not in reeks:
        print(f"{nummer} bestaat niet in de reeks...")
    else:
        for x in reeks:
            if nummer == reeks:
                x - 1
                print(reeks[x])


