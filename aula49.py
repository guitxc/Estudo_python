'''
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimento reutilizavel - indices e fatialemnte
Metodos uteis: append, insert, pop, del, clear, extend +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
#        0   1   2   3
# Prestar atenção lista comsome muito processamento !!! evitar
lista = [10, 20, 30, 40, 50, 60, 70]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # adiciona ao final, pode colocar quantos quiser,/
# não gasta tanto processamento
ultimo_valor = lista.pop() # remove o ultimo digito

print(lista, 'Removido', ultimo_valor)