# try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else: # sera executado se não tiver erro
    print('Nao deu erro') 
finally: # O finally sempre sera executado, mesmo apos o erro
    print('Fechar arquivo')
    