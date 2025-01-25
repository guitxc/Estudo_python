# Listas de listas e seus indices
# Um iteravel dentro do outro


salas = [
    # 0           1
    ['Maria', 'Helena'], # 0
    # 0
    ["Elaine",'Ronaldo' ], # 1
    #  0
    ['Luiz', 'Joao', 'Eduarda', (0,10,20,30,40)] # 2
]

print(salas)
print('---------------------')
print(salas[0][1])
print('---------------------')
print(salas[1][1])
print('---------------------')
print(salas[2][2])
print('---------------------')
print(salas[2][3][2])
print('---------------------')

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)