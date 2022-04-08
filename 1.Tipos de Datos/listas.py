#Listas son secuencias ordenadas que guardan una variedad de tipos de objeto
#Usan [] braquets y comas para separar objetos en una lista [1,2,3,4,5]
#Son mutables
#Las listas soportan Indices y Slicing
#Puedes tener listas adentro de listas y pueden guardar metodos que pueden ser llamados

#mi_lista = [1,2,3]
#mi_lista = ['Cadena', 3, 4]
mi_lista = ['uno', 'dos', 'tres']

otra_lista = ['cuatro', 'cinco', 'seis']

nueva_lista = mi_lista + otra_lista

nueva_lista[0] = 'Ileana' #Cambiar indice 0

nueva_lista.append('siete') #Concatenacion

item_pop = nueva_lista.pop(-1) #elimina el último elemento de un array y devuelve su valor al método que lo llamó

print(mi_lista)
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[1:]) #Imprime del objeto uno hacia adelante
#print(mi_lista + otra_lista)
print(nueva_lista)
print(item_pop)

lista_letra = ['a', 'z', 'x', 'b','d']
num_lista = [4,1,5,7,3]

lista_letra.sort() #ordena los elementos de un arreglo (array) localmente y devuelve el arreglo ordenado
lista_letra.reverse()

print(lista_letra)