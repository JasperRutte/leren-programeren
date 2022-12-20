def fibo(nummer: int):
    nieuw = 1
    oud = 0
    oud2 = 0
    reeks = []
    test = []
    for x in range(0, 100):
        reeks.append(oud)
        oud = nieuw
        nieuw += oud2
        oud2 = oud

    if nummer not in reeks:
        print(f"{nummer} zit iet in reeks")
    elif nummer in reeks:
        for x in range(0, len(reeks)):
            if reeks[x] == nummer:
                for y in range(x-1, len(reeks)):
                    test.append(reeks[y])
    return test

print(fibo(55))
