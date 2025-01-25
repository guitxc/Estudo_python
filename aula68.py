import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

multiplicador_1 = 10

resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * multiplicador_1
    multiplicador_1 -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Digito 2 

dez_digitos = nove_digitos + str(digito_1)
multiplicador_2 = 11
resultado_2 = 0

for digito in dez_digitos:
    resultado_2 += int(digito) * multiplicador_2
    multiplicador_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

print(cpf_gerado_pelo_calculo)