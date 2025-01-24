"""
Exercicio
Exiba os indices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria',  'Helena', 'Luiz']
lista.append('João')
lista.append('Gui')

i = range(len(lista))

for indice in i: 
    print(i, lista[indice],  type(lista[indice]))