# Exercicio - adiando execução de funções
def soma (x , y):
    return x + y

def mulplica (x , y):
    return x * y

def executa (funcao, x): #closures
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = executa(soma, 5)
mulplica_por_dez = executa(mulplica, 10)
print(soma_com_cinco(10))
print(mulplica_por_dez(10))