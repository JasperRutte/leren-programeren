def fibo(nummer: int):
    reeks = [0, 1]
    user_reeks = []
    for x in range(0, 50):
        reeks.append(reeks[-2] + reeks[-1])

    if nummer not in reeks:
        print(f"{nummer} zit iet in reeks")
    elif nummer in reeks:
        for x in range(0, len(reeks)):
            if reeks[x] == nummer:
                for y in range(x, x + 10):
                    user_reeks.append(reeks[y])
    return user_reeks


print(fibo(55))


# extra opdracht van fibonacci
def fibo(nummer: int):
    reeks = [0, 1]

    for x in range(0, 100):
        reeks.append(reeks[-2] + reeks[-1])

    if nummer not in reeks:
        print(f"{nummer} zit niet in reeks")
    elif nummer in reeks:
        print(reeks[0:reeks.index(nummer) + 1])


fibo(0)
