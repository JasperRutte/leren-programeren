from functions import *
from data import *

print('Welkom bij Papi Gelato!')
print('')

while ordering:
    askUserIfBusiness = askUser('Bent u \n\nA) een particuliere klant \nB) een zakelijke klant?', ['a', 'b'])
    if askUserIfBusiness == 'a':
        inputAmount = integerInput('Hoeveel bolletjes wilt u? ')
        if inputAmount > 8:
            print('Zulke grote bakjes hebben wij niet.')
            continue
        elif inputAmount <= 0:
            print('Dat zijn te weinig bolletjes.')
            continue
        else:
            if inputAmount <= 3:
                bakjeHoorntje = askUser('Wilt u een bakje of een hoorntje? ', ['bakje', 'hoorntje'])
            else:
                bakjeHoorntje = 'bakje'

            for item in range(1, inputAmount + 1):
                iceCreamInput = askUser(
                    f'Welke smaak wilt u voor bolletje nummer {item}? \nA) Aardbei \nC) Chocolade \nM) Munt \nV) Vanille? ',
                    ['a', 'c', 'm', 'v'])
                iceCreamReceived = receivedIceCream(iceCreamInput)

                if item == inputAmount:
                    skipTables = True
                    iceCreamToppingInput = askUser(
                        f'Wat voor topping wilt u: \nA) Geen \nB) Slagroom \nC) Sprinkels \nD) Caramel Saus?',
                        ['a', 'b', 'c', 'd'])
                    iceCreamToppingReceived = receivedIceCreamTopping(iceCreamToppingInput)
                else:
                    iceCreamToppingReceived = 'None'
                    skipTables = False

                adaptedPrices = changeVariables(prices, bakjeHoorntje, iceCreamReceived, iceCreamToppingReceived,
                                                skipTables)
        if iceCreamToppingReceived == 'Geen':
            print(f'Dan krijgt u van mij een {bakjeHoorntje} met {inputAmount} bolletjes')
        else:
            print(
                f'Dan krijgt u van mij een {bakjeHoorntje} met {inputAmount} bolletjes en een topping van {iceCreamToppingReceived}')
        print(f'Hier is uw {bakjeHoorntje} met {inputAmount} bolletjes')

        ordering = askUser('Wilt u nog een keer bestellen? (J/N) ', ['j', 'n']) != 'n'
    elif askUserIfBusiness == 'b':
        inputAmount = integerInput('Hoeveel liter ijs wilt u? ')
        for item in range(1, inputAmount + 1):
            iceCreamLiterInput = askUser(
                f'Welke smaak wilt u voor liter ijs ({item})? \nA) Aardbei \nC) Chocolade \nM) Munt \nV) Vanille? ',
                ['a', 'c', 'm', 'v'])
            iceCreamReceived = receivedIceCreamLiter(iceCreamLiterInput)

            adaptedPrices = changeVariablesLiter(prices, iceCreamReceived)

        ordering = False

newPrices = checkBill(adaptedPrices)
billData = receiveBillData(adaptedPrices, newPrices)

print()
if len(billData) >= 1:
    print(f'---------["Papi Gelato"]---------')
    for item in billData:
        itemName = item['name']
        itemAmount = item['totalAmount']
        itemPrice = item['price']
        itemTotalPrice = item['totalPrice']
        totalPrice = totalPrice + itemTotalPrice
        print(f'{itemName}    {itemAmount} x € {itemPrice} = € {itemTotalPrice}')
    print(f'                    ------ +')
    if askUserIfBusiness == 'b':
        totalBTW = totalPrice / 100 * btwNumber
        print(f'BTW ({btwNumber}%)          = € {round(totalBTW, 2)}')
    print(f'Totaal            = € {round(totalPrice, 2)}')

    print(f'')
    print(f'Bedankt en tot ziens!')
else:
    print(f'Tot ziens!')