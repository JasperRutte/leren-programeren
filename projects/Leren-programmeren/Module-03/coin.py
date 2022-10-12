# name of student: Jasper Rutte
# number of student: 99071902
# purpose of program: To see how much change to give and how much change you gave
# function of program: calculate how much change to give, how much change has been given and how much change you should've payed
# structure of program:

toPay = int(float(input('Amount to pay: ')) * 100)  # toPay is a user input * 100
paid = int(float(input('Paid amount: ')) * 100)  # paid is a user input * 100
change = paid - toPay  # change is var paid - var toPay
amountReturned = ""
payed = [500, 300, 200, 50, 20, 10, 5, 2, 1]
payedString = ""

if change > 0:  # check if var change is greater than 0
    coinValue = 500  # giving coinValue a value

    while change > 0 and coinValue > 0:  # check if change is greater than 0 and coinValue is greater than 0
        nrCoins = change // coinValue  # var nrCoins is change divided by coinValue with extra's
        if nrCoins > 0:  # check if nrCoins is greater than 0
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')  # print a string
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))  #
            change -= nrCoinsReturned * coinValue  #
            amountReturned += str(coinValue) + " x" + str(nrCoinsReturned) + "\n"

        # comment on code below:
        if coinValue == 500:
            coinValue = 300
        elif coinValue == 300:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 50
        elif coinValue == 50:
            coinValue = 20
        elif coinValue == 20:
            coinValue = 10
        elif coinValue == 10:
            coinValue = 5
        elif coinValue == 5:
            coinValue = 2
        elif coinValue == 2:
            coinValue = 1
        else:
            coinValue = 0

if change > 0:  #
    print('Change not returned: ', str(change) + ' cents')

else:
    print('done')
print(amountReturned)

while change > 0:
    for x in payed:
        change = change // x
        print(f"{x} x{change}")
