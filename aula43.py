# texto = 'python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i])

#     i += 1

texto = 'python'
texto1 = ''

for letra in texto:
    print(letra) 

for letra1 in texto:
    texto1 += f'*{letra1}'
    print(letra1)
print(texto1)