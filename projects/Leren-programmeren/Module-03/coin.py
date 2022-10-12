# name of student:
# number of student:
# purpose of program:
# function of program:
# structure of program:

toPay = int(float(input('Amount to pay: ')) * 100)  #
paid = int(float(input('Paid amount: ')) * 100)  #
change = paid - toPay  #
amountReturned = ""
payed = [500, 300, 200, 50, 20, 10, 5, 2, 1]
payedString = ""

if change > 0:  #
    coinValue = 500  #

    while change > 0 and coinValue > 0:  #
        nrCoins = change // coinValue  #

        if nrCoins > 0:  #
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')  #
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
