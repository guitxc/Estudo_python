'''
Higher Order Functions
Funções de primeira classe
'''


def saudacao(msg, nome):
    return msg, nome


def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia','Gui')
print(v)