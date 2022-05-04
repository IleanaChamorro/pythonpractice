
milista= [1,2, 3]

#Tipo range se utiliza para representar una secuencia inmutable de números. 

#for num in range(0,11,2):
#    print(num)

#Poner rango en una lista
print(list(range(0,11,2)))

#Imprimir valores en una lista
contador_indice = 0
palabra = 'Hola'

for letter in palabra:
    print(palabra[contador_indice])
    contador_indice += 1

palabra = 'Python'

for index,letter in enumerate(palabra):
    print(index)
    print(letter)


#milista1 = [1,2,3,4,5,6]
#milista2 = ['a', 'b', 'c']
#milista3 = [100, 200, 300]

#Iteración a través de items
#for item in zip(milista1, milista2, milista3):
#    print(item)

#Función zip
#El iterador devuelto se devuelve como una tupla como una lista, un diccionario o un conjunto. En esta tupla, los primeros elementos de ambos iterables se emparejan.

#Iterar una lista usando list
#milista1 = [1,2,3,4,5,6]
#milista2 = ['a', 'b', 'c']
#d = {'k1':1}
#milista3 = [100, 200, 300]

#if 'k1' in d:
#    print('Verdadero')

#if 1 in d.keys():
#    print('Verdadero')
#else:
#    print('Falso')

#Minimos y Maximos de lista
#print(max(milista1))
#print(min(milista1))


#Mezclar una lista (reorganizar el orden de los elementos de la lista):
#from random import shuffle

#milista1 = [1,2,3,4,5,6]
#milista2 = ['a', 'b', 'c']
#d = {'k1':1}
#milista3 = [100, 200, 300]

#print(shuffle(milista1))

resultado = input('Escribe un numero aqui: ')

#Convertir a numero entero
print(type(float(resultado)))