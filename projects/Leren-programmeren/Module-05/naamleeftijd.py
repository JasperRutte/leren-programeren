def names_ages():
    lst = []
    dct = {}
    stop = True
    while stop:
        name = input("Naam: ")
        if name == "stop":
            for people in lst:
                print(people["name"] + " is " + people["age"] + " jaar")
            return
        else:
            dct.update({"name": name})
        age = input("Leeftijd: ")
        if age == "stop":
            for people in lst:
                print(people["name"] + " is " + people["age"] + " jaar")
            return
        else:
            dct.update({"age": age})
        lst.append(dct)
        dct = {}


names_ages()
