frase = 'O Python é uma liguagem de programação' \
    'muiltipradgma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_atual = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qnt_vezes_letra_apareceu = frase.count(letra_atual)

    if qtd_atual < qnt_vezes_letra_apareceu:
        qtd_atual = qnt_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi ')
print(f'{letra_apareceu_mais_vezes} que apareceu')
print(f'{qtd_atual}x')