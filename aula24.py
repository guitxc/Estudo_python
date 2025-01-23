# Operadores in e not in
# Strings são iteraveis = pode navegar item por item
#  0 1 2 3 4 5 6 7 8
#  G u i l h e r m e
# -9-8-7-6-5-4-3-2-1
# in = esta entre e not in = não esta entre
# nome = 'Guilherme'
# print(nome[0])
# print(nome[-8])
# print('Gui' in nome)
# print('me' in nome)
# print(5 * '-')
# print('i' not in nome)
# print('a' not in nome)
nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')