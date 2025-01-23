"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
O CONTINUE É PARA RECOMEÇAR O LOOP
"""
# palavra = 'receba'
# palavra_escondida = '******'
# while letra_input != palavra:
#     letra_input = input('Digite uma letra')
#     if len(letra_input) > 1:
#         print('Digite apenas uma letra')
# else:
#     print(palavra_escondida)

import os # 'os' faz interações com o sistema

palavra_secreta = 'receba'
letras_corretas = ''
tentativas = 1

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    if tentativas > 100:
        print('Uau, voce ja esta na tentativa numero: ', tentativas)

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!.')
        continue

    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada ', palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABENS!!')
        print('A palavra era ', palavra_secreta)
        print('Tentativas:', tentativas)
        letras_corretas = ''
        tentativas = 0
    
