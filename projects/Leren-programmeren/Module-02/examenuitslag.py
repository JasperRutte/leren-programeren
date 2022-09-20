def numberCheck(score: str) -> int:
    try:
        aantal = int(input(score))
    except ValueError:
        print("Gebruik alleen HELE getallen!")
        return numberCheck(score)
    return aantal


scoreE = numberCheck("Wat is scoreE: ")
scoreP = numberCheck("Wat is scoreP: ")
scoreO = numberCheck("Wat is scoreO: ")
scoreS = numberCheck("Wat is scoreS: ")


if scoreP == 8 and scoreE > 4 and scoreO == 0 and scoreS == 0:
    print("Je hebt een goed")
elif scoreP + scoreE - scoreO == 8 and scoreS == 0 or scoreS == 1 and scoreP + scoreE - scoreO > 9:
    print("Je hebt een voldoende")
else:
    print("Je bent gezakt")


    # What kind of house?
    # How many rooms / what kind of rooms?
    # What is your most favourite place at home? Why?
    # Do you have a balcony / garden? etc.
    # Describe the interior of one room.