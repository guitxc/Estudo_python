lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

# for utilizando list comprehesion
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [letra for letra in 'Guilherme']
    for x in range(3)
]

print(lista)