'''
iteravel -> str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega o iterador me intrega o interador
'''
# texto = iter('Gui') #__iter__()

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())


# for letra in texto
texto = 'Luiz' # iteravel
# iterador = iter(texto) # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break 

for letra in texto:
    print(letra)