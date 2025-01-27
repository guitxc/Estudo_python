'''
Closeru e funções que retornam outras funções
'''


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


s1 = criar_saudacao('Bom dia', "Guilherme")
s2 = criar_saudacao('Boa noite', "Guilherme")

print(s1()) # closeru
print(s2())

