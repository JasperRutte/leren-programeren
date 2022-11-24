from fruitmandplus import fruitmand

a = 0
fruitmand.append({'name': 'watermeloen', 'weight': 2000, 'color': 'green', 'round': True})

for i in fruitmand:
    b = i['weight']
    a += b
print(a)
