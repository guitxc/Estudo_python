'''
Valores padrão para paremtros
Ao  definir uma função, os paramentros podem
ter valores padrao. Caso o valor nao seja
enviado para o parametro, o valor padrao sera
usado
Refatorar = editar o seu codigo
'''

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} ', x + y)


soma(2,3)
soma(4,6)
soma(100, 200, 0)
soma(42, 654, 4)
soma(y=42, z=654, x=4)