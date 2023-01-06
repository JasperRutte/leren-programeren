def fibo(nummer: int):
    nieuw = 1
    oud = 0
    oud2 = 0
    reeks = []
    test = []
    for x in range(0, 50):
        reeks.append(oud)
        oud = nieuw
        nieuw += oud2
        oud2 = oud

    if nummer not in reeks:
        print(f"{nummer} zit iet in reeks")
    elif nummer in reeks:
        for x in range(0, len(reeks)):
            if reeks[x] == nummer:
                for y in range(x, x + 10):
                    test.append(reeks[y])
    return test


print(fibo(1))


def fibo2(nummer: int):
    nieuw = 1
    oud = 0
    oud2 = 0
    reeks = []
    test = []
    for x in range(0, 50):
        reeks.append(oud)
        oud = nieuw
        nieuw += oud2
        oud2 = oud
    if nummer not in reeks:
        print(f"{nummer} zit niet in de reeks...")
    else:
        for x in reeks:
            if x == nummer:
                test.append(x)
                return test
            else:
                test.append(x)


print(fibo2(5))
