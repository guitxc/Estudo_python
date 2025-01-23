'''
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
'''
numero = input('Vou dobrar o numero que voce digitar:')

try:
    numero_float = float(numero)
    print('STR: ', numero)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero')




# print(numero.isdigit())

# if numero.isdigit():
#     numero_float = float(numero)
# else:
#     print('Isso não é um numero')

# print(f'O dobro de {numero} é {numero_float * 2:.2f}')
