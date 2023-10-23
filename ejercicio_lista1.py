x=int(input("por favor ingrese un numero para calcular:"))
x2=int(input("ingrese segundo digito:"))
lista=[]
for i in range(1,x2+1):
    lista.append(x*i)
print(lista)