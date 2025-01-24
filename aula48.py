'''
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimento reutilizavel - indices e fatialemnte
Metodos uteis: append, insert, pop, del, clear, extend +
'''
#        +01234
string = 'ABCDE' # 5 caracteres
#        -54321
lista = list()
lista1 = [] # ""
print(lista1, type(lista1))
print(bool([])) # falsy
#          0     1     2     3   4
lista2 = [123, True, 'Gui', 1.2, []]
print(lista2)
print(lista2[2].upper(), type(lista2[2]))

lista2[-3] = 'Ronaldo'
print(lista2[2].upper(), type(lista2[2]))

