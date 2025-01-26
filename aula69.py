'''
Introdução as funçoes (def) em python
Funções são trechos de codigo usados para
replicar determinada ação ao longo do seu codigo
Elas podem receber valores para parametros (argumentos)
e retonar um valor especifico
Por padrao, funções Python retornam None (nada)
'''
# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Ola, {nome}!')

saudacao('Gui')
saudacao()