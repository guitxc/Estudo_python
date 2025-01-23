nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
# Se nome e idade forem True entao faz o if se nao faz o else
if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1::-1]}')
    if ' ' in nome:
        print(f'Seu nome tem espaço ')
    else:
        print('Seu nome não tem espaço')
    print(f'Seu nome {nome} tem {len(nome)} de letras ')
    print(f'Seu nome {nome} começa com {nome[0]} de letras ')
    print(f'Seu nome {nome} começa com {(nome)[-1]} de letras ')
else:
    print('Nada foi digitado')
    

