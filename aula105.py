# Yield from
def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1() # posso continuar um yield da onde a outra função parou!
    yield 4
    yield 5
    yield 6

g = gen2()
for numero in g:
    print(numero)
