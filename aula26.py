'''
Formatação basica de strings
s - strings
d - int
f - float
.<numero de digitos>f
x ou X - hexadecimal
(Caractere)(><^(quantidade)
> - esquerda
< - Direito
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr__ __str__ __ask__
'''
variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
print(f'{variavel: ^10}.')
print(f'{1000.8124247472:+,.1f}')
print(f'{-1000.8124247472:-,.1f}')
print(f'{+1000.8124247472:0>+10,.1f}')
print(f'{+1000.8124247472:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')