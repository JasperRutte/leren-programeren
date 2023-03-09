def integerInput(prompt : str) -> int:
    while True:
        inputAmount = input(prompt)
        try:
            inputAmount = int(inputAmount)
            return inputAmount
        except ValueError:
            print('Sorry, dit herken ik niet!')

def askUser(prompt : str, data : list) -> str:
    while True:
        inputQuestion = input(prompt).lower()
        if inputQuestion in data:
            return inputQuestion
        else:
            print('Sorry, dit herken ik niet!')

def changeVariables(list : list, providedType : str, iceCreamReceived : str, iceCreamTopping : str, skipTables : bool) -> list:
    for price in list:
        if price['name'] == providedType:
            if skipTables:
                price['totalAmount'] = price['totalAmount'] + 1
        elif price['name'] == iceCreamReceived:
            price['totalAmount'] = round(price['totalAmount'] + 1, 2)
        elif price['label'] == iceCreamTopping:
            if iceCreamTopping == 'Caramel Saus':
                if providedType == 'bakje':
                    price['price'] = 0.90
                elif providedType == 'hoorntje':
                    price['price'] = 0.60

            price['totalAmount'] = round(price['totalAmount'] + 1, 2)
    return list


def changeVariablesLiter(list: list, iceCreamReceived: str) -> list:
    for price in list:
        if price['name'] == iceCreamReceived:
            price['totalAmount'] = round(price['totalAmount'] + 1, 2)
    return list

def checkBill(list : list) -> list:
    emptyList = []
    for price in list:
        if price['totalAmount'] >= 1:
            emptyList.append(price['name'])
    return emptyList

def receiveBillData(originalData : list, deliveredData : list) -> list:
    emptyList = []
    for item in originalData:
        if item['name'] in deliveredData:
            data = {
                'name': item['name'].capitalize(),
                'price': item['price'],
                'totalPrice': round(item['price'] * item['totalAmount'], 2),
                'totalAmount': item['totalAmount']
            }
            emptyList.append(data)
    return emptyList

def receivedIceCream(item : str) -> str:
    if item == 'a':
        return 'Aardbei'
    elif item == 'c':
        return 'Chocolade'
    elif item == 'm':
        return 'Munt'
    elif item == 'v':
        return 'Vanille'

def receivedIceCreamTopping(item : str) -> str:
    if item == 'a':
        return 'Geen'
    elif item == 'b':
        return 'Slagroom'
    elif item == 'c':
        return 'Sprinkels'
    elif item == 'd':
        return 'Caramel Saus'

def receivedIceCreamLiter(item: str) -> str:
    if item == 'a':
        return 'L.aardbei'
    elif item == 'c':
        return 'L.Chocolade'
    elif item == 'm':
        return 'L.Munt'
    elif item == 'v':
        return 'L.Vanille'

