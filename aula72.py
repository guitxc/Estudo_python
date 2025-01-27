'''
Escopo de funções em Pyhon
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e o local
O escopo global é o escopo onde todo o codigo é alcancavel
O escopo local é o escopo onde fica apenas nomes do mesmo local
podem ser alcaçados
'''
x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)