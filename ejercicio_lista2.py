#ingresa numero a una lista hasta que el digito que se coloque sea cero
lista=[]
while True:
    numero=int(input('ingrese numero: '))
    if numero==0:
        break
    else:
        lista.append(numero)
lista.sort()
print(lista)