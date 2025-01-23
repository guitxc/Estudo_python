primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o seu segundo valor {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o seu primeiro valor {primeiro_valor}')
else:
    print(f'Os valores {primeiro_valor} e o {segundo_valor} são iguais')