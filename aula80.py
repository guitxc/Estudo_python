# Exercicos
# Crie funções que duplicam, triplicam e quadruplicam
# o numero recebido como parametro

# def duplicar(x):
#     return x * 2
# def triplicar(x):
#     return x * 3
# def quadruplicar(x):
#     return x * 4

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

