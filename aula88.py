perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Qual a capital da França?',
        'Opções': ['Londres', 'Paris', 'Berlim', 'Roma'],
        'Resposta': 'Paris'
    }
]

pontuacao = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i+1}. {opcao}")

    escolha = input("Digite o número da resposta: ")

    if pergunta['Opções'][int(escolha) - 1] == pergunta['Resposta']:
        print("Correto!\n")
        pontuacao += 1
    else:
        print("Errado!\n")

print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
