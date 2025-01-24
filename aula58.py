'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de inserir
apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
'''
import os
lista_de_compras = []
while True:
    print('--Selecione uma opção--')
    comando = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
    # Inserir
    if comando == 'i':
        os.system('cls')
        inserir = input('Qual item deseja adicionar? ')
        lista_de_compras.append(inserir)
        continue
    # Apagar
    elif comando == 'a':
        os.system('cls')
        apagar_item = input('Qual o indice do item que deseja apapar? ')
        try:
            lista_de_compras.pop()
        except:
            print('Esse indice não existe')
   # Listar
    elif comando == 'l':

        os.system('cls')

        if len(lista_de_compras) == 0:
            print('Lista vazia')
        for indice, item in enumerate(lista_de_compras):
            print(indice, item)
    # Sair
    elif comando == 's':
        break
    
    else:
        os.system('cls')
        print('Esse comando não existe')