# cijfers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# for x in cijfers:
#     print(f"Tafel van{x}")
#     for y in cijfers:
#         print(f"{x} * {y} = {x * y}")

nummers = [5, 12, 19, 27, 3]
nummers.append(25)

print(len(nummers))

print(nummers)
nummers.pop(1)
print(nummers)

print(nummers)
nummers.pop(0)
print(nummers)

print(nummers)
nummers.insert(0,36)
print(nummers)

a = 0
for i in nummers:
    a += i
print(a)

nummers.clear()
print(nummers)

for i in range(1, 4):
    nummers.append(i)

for i in range(4, 51):
    nummers.append(i)
print(nummers)

print(nummers[25])


print(nummers)
nummers.
print(nummers)
