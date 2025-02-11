import sys


# Generator expression, iterables e Iterators em python
# Generator geralmente são fuçoes que sabem pausar
# Todo generator é um iterator, mas todo iterator não é um generator
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(1000000)]
# a partir do momento que criamos uma lista todos os dados são armazenados 
generator = (n for n in range(1000000))
# o generator esta esperando pedir um valor
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(generator)