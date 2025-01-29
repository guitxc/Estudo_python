# Exemplos de uso dos sets
letras = set()
while True:
    letra = input('Digito: ')
    letras.add(letra.lower())

    if 'g' in letras:
        print('PARABENS VOCE ENTROU O g')
        break

    print(letras)