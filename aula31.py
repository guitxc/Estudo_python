"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
print(id(v1))
v2 = 'a'
print(id(v2))


condição = True
passou = None
if condição:
    passou = True
    print('faça algo')
else:
    print('Nao faça algo')

print(passou, passou is None)
print(passou, passou is  not None)