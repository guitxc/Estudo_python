'''
# Função lambda em python
A função labda é uma função como qualquer outra
em Python. Porem, são funções anônimas que 
contem apenas uma linha. Ou seja, tudo deve ser
contido detro de uma nuica expressão
 Lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'}
    {'nome': 'Hugo', 'sobrenome': 'Alves'}
    {'nome': 'Gui', 'sobrenome': 'Silva'}
    {'nome': 'Joao', 'sobrenome': 'Freitas'}
    {'nome': 'Cleber', 'sobrenome': 'Python'}
]
'''
# lista = [4, 1,2,3,4,5,8,24,9,12,23,34,134,44,24]
# lista.sort() # Modifica a lista e deixa ordenada
# lista.sort(reverse=True)
# # sorted(lista) cria uma nova lista ordenada


# print(lista)


lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Hugo', 'sobrenome': 'Alves'},
    {'nome': 'Gui', 'sobrenome': 'Silva'},
    {'nome': 'Joao', 'sobrenome': 'Freitas'},
    {'nome': 'Cleber', 'sobrenome': 'Python'},
]
def exibir(lista):
    for item in lista:
        print(item)
    print()
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)