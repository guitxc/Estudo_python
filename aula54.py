# Intridução ao desempacotamento + tuples (tuplas)

# nomes = ['Maria',  'Helena', 'Luiz']
# nome1,  nome2, nome3 = ['Maria',  'Helena', 'Luiz']
# print(nome2)
_ , nome2, *_ = ['Maria',  'Helena', 'Luiz'] # *para armazenar o resto,
# _ para mostrar que não irei usar
print(nome2, _)
