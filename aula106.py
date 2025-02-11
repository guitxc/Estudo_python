# Try, except, else e finally

try:
    a = 18
    b = 0
    print('linha 1.'[1000])
    c = a / b
    print('linha 2.') # pula direto para o except

except ZeroDivisionError:
    print('Dividiu por zero!.')
except NameError:
    print('Não esta definido')
except (TypeError, IndexError) as error: # Jogar a instancia em uma variavel
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception: # Trata todos os outros erros
    print('Erro desconhcido')

print('Continuar')