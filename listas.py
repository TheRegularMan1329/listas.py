#[]=arreglo
lista=[]
lista=[1,5,10,50,100,500]
#numero positivo= cuenta desde el cero hacia el final
#numero negativo= Cuenta desde el ultimo hasta el principion
print(lista[-1])

#append= agregar dato en la ultima posicion de la lista
lista.append(1000)
print(lista[-1])

#Extends= Permite fusionar una lista con otra
lista2=[5000,9999]
lista.extend(lista2)
print(lista)

#Insert(posicion,dato)= insertar un dato en la posicion especifica
lista.insert(4,99)
print(lista)

#Remove(dato)= Elimina un dato de la lista
lista.remove(99)
print(lista)

#pop()= Elimina el ultimo registro de la lista
#pop(posicion)= Elimina la posicion indicada
lista.pop()
print(lista)

#reverse= invierte el orden de los datos
lista.reverse()
print(lista)

#sort= ordena lista de menor a mayor
lista.sort()
print(lista)

#sort(reverse=true)= Ordena lista de mayor a menor
lista.sort(reverse=True)
print(lista)