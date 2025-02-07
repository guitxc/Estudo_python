# Generator expression, iterables e Iterators em python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator)) # esgota os valores