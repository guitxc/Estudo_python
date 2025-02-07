# dir, hsattr e getattr em python
# dir checka os atributos no debbuger console
string = 'Guilherme'
metodo = 'upper'
if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else: print('Não existe o metodo', metodo)