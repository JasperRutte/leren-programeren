getal = 50
som = 50
layout = '50 '

while som < 1000:
    getal += 1
    som += getal
    layout += f'+ {getal} '
    print(f'{layout} = {som}')
