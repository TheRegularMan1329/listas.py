# calcula suma y promedio de n numeros ingresados a una lista.
lista=[]
suma=0
n=int(input('ingrese cantidad de numeros: '))
for i in range(1,n+1):
    x=int(input('ingrese numero: '))
    lista.append(x)
for i in range(1,n+1):
    suma=suma+lista[i-1]
print(suma)
print(suma/10)