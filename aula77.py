'''
Exercicicos com funções

Crie umaf função que multiplica todos os argumentos
Não nomeados recebidos
Retorte o total para uma variavel e mostre o valor
da variavel

Crie uma função fala se um numero é par ou impar.
Retorne se o numero é par ou impar
'''

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao_2_5_2 = multiplicacao(2,5,2)
print(multiplicacao_2_5_2)
print(2*5*2)

def par_ou_impar(x):
    if x % 2 == 0:
        return f'O numero {x} é par'
    return f'O numero {x} é impar'

par_ou_impar_2 = par_ou_impar(2)
print(par_ou_impar_2)