# Manipulando chaves e valores em dicionarios

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Guilherme'
pessoa['sobrenome'] = 'Receba'


print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Jao'

del pessoa['sobrenome']
print(pessoa)

pessoa.get('sobrenome')

if pessoa.get('sobrenome') is None:
    print('Existe')
else:
    print(pessoa['sobrenome'])

print(pessoa[chave])