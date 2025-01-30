# List comprehesion em python
# List comprehesion é uma forma rapida para criar listas
# a partir de iteraveis.
# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)
print(lista)

lista1= [
    numero * 2 
    for numero in range(10)
]
print(lista1)
