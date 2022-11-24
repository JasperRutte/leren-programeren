from fruitmandplus import fruitmand

for i in fruitmand:
    if i['name'] == 'druif':
        fruitmand.remove(i)

for i in fruitmand:
    print(i['color'])
