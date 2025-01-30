# Empacotamento e desempacotamento de dicionarios
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Guizim',
    'sobrenome': 'Python',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# args e kwargs
# args (ja vimos)
# kwargs - keyword arguments (argumentos nomeados) **
def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa)