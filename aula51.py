lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # não retorna a nada, mexe diretamente
# com a lista_a
print(lista_a, lista_d)