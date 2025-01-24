# enumarate - enumera iteraveis (indices)

lista = ['Maria',  'Helena', 'Luiz']
lista.append('João')
lista.append('Gui')

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)


for item in lista_enumerada: # nao da pois ele ja consumiu os valores
    print(item)


for item in enumerate(lista): # assim é possivel
    print(item)

for item in enumerate(lista, start=20):
    print(item)

for item in enumerate(lista):
    a, b = item
    print(a,b)

for a, b in enumerate(lista):
    print(a,b)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}') # \t é tab