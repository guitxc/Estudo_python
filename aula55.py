"""
Cuidados com dados mutaveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
nome = 'Luiz'
noutra_variavel = nome
nome = 'Joao'
print(nome) # tem ids diferentes
print(noutra_variavel)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a # tem o mesmo id
lista_c = lista_a.copy() # copia a lista como ela esta no momento
lista_a[0] = 'Qualquer coisa' # modifica o valor
print(lista_a)
print(lista_b)
print(lista_c)
