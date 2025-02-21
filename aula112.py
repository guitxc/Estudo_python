import importlib
import aula112_m # modulos em python sao singonton

print(aula112_m.variavel)

for i in range(10):
    importlib.reload(aula112_m) # recarrega o  modulo
    print(i)

print('fim')