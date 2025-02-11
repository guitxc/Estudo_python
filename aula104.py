# Introdução às Generator functions em Python
# Toda Generator functions utiliza a função yield no lugar do return
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1 # Pausa a execução da função
    print('yield 1!!!')
    yield 2
    print('yield 2!!')
    yield 3
    print('yield 3!')
    return 'Acabou' # return levanta uma exeção de stop iteration
gen = generator(n=0)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)


def generator_2(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen_2 = generator_2(n=5, maximum=8)
for n in gen_2:
    print(n)