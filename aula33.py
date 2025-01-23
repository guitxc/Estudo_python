# Imutaveis que vimos str, int, float, bool são objetos

string = 'guilherme'
outra = f'{string[:3]}ABC{string[4:]}'
print(outra)
print(string[3])
print(string.capitalize())
print(string.zfill(10))

# str.capitalize()
# Retorna uma cópia da string com o seu primeiro caractere em maiúsculo
# e o restante em minúsculo