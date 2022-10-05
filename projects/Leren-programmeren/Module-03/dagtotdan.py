week = ["ma","di","wo","do","vr","za","zo"]
dag = input("Geef een dag van de week op: ")

while dag != week[0]:
    print(week[0])
    week.pop(0)
