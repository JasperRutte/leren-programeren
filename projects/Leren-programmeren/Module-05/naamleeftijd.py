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



lst = []
again = True


def name_age():
    dct = {}
    name = input("Name: ")
    if name == "stop":
        return name
    age = input("Age: ")
    if age == "stop":
        return age

    dct.update({"Name": name})
    dct.update({"Age": age})
    return dct


while again:
    again = name_age()
    if again == "stop":
        break
    else:
        lst.append(again)

name_age()
