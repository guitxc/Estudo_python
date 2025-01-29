'''
Metodos uteis dos diconarios em python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave nao existe
copy - retotrna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
'''

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
print(p1.get('nome'))
print(p1.get('nome', 'Nao existe'))

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)


p1.update({
    'idade': 30,
    'altura':1.70,
})
tupla = ('nome', 'novo valor'), ('idade', 30)


print(p1)