"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um numero inteiro: ')
# print(type(numero))
# try:
#     numero = int(numero)
#     if numero % 2 == 0:
#         print(f'Seu numero {numero} é par')
#     else:
#         print(f'Seu numero {numero} é impar')
# except:
#     print('Seu numero não é inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# qual_hora = input('Qual é a hora agora? ')
# try:
#     qual_hora_int = int(qual_hora)
#     if qual_hora_int >= 0 and qual_hora_int <= 11:
#         print('Bom dia!!!')
#     elif qual_hora_int >= 12 and qual_hora_int <= 17:
#         print('Boa tarde!!!!')
#     elif qual_hora_int >= 18 and qual_hora_int <= 23:
#         print('Boa noite!!!!!!')
#     else:
#         print('Essa hora não existe')
# except:
#     print('Horaio invalido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Qual o seu nome? ')
try:
    qntd_letras = len(nome)
    
    if qntd_letras <= 4:
        print("Seu nome é curto")
    elif qntd_letras >= 5 and qntd_letras <= 6:
        print("Seu nome é normal")
    elif qntd_letras >= 7:
        print("Seu nome é grande")
    else:
        ...
except:
    print('Nome invalido, esse realmente é seu nome??')