'''
Argumetos nomeados e não nomeados em funções Python
Argumentos nomeado tem nome com sinal de igual
Arguemnto não nomeado recebe apenas o argumento (valor)
'''
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z =', x + y + z)




print(soma)
print(soma(1,2, 3))
(soma(1,2, 3))
(soma(y=1,x=2, z=3))
soma(1, 2 , z=5)
