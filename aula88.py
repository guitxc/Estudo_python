# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set() # vazio
# s2 = {'Gui', 1, 2, 3} # com dados
# print(s1, type(s1))
# print(s2, type(s2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# print(l1)
# l2 = list(s1)
# print(l2) # Nao garante a ordem

# s2 = { 1, 2, 3, 3, 3, 3, 1}
# print(s2) # nao repeti valores

# s1 = s1 = {1, 2, 3, (123, 456)} # apenas tipos imutaveis dentro do set
# print(s1)

# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz') # só adiciona um valor por vez
s1.add(123)
s1.update('Ola') # adiciona o item iterado letra por letra
s1.update(('Ola', 1, 2))
# s1.clear() # limpa os valores
s1.discard('O') # retira apenas um valor
s1.discard('l')
s1.discard('a')
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s2 = {1, 2, 3}
s3 = {2, 3, 4}
s4 = s2 | s3
s5 = s2 & s3
s6 = s2 - s3
s7 = s2 ^ s3
print(s4)
print(s5)
print(s6)
print(s7)