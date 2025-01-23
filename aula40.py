'''
calculadora com while
'''
while True:
    print('---Calculadora---')
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite o operador: ')

    num_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os numeros digitados são invalidos')
        continue

    operadores_validos = '+-*/'


    if operador not in operadores_validos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    resutado = 0
    if operador == '+':
        resutado = num1_float + num2_float
    elif operador == '-':
        resutado = num1_float - num2_float
    elif operador == '*':
        resutado = num1_float * num2_float
    elif operador == '/':
        resutado = num1_float / num2_float

    print(f'Seu resultado é {resutado}')

    sair = input('Quer sair? [s]: ')
    sair = sair.lower()
    sair = sair.startswith('s')
    if sair:
        break