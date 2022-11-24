from fruitmandplus import fruitmand

a = sorted(fruitmand, key=lambda i: i['weight'])
for i in a:
    print(f'{i["name"]}: {i["weight"]}')
