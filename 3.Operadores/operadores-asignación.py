#Un operador de asignación, como su nombre lo indica, se encarga de asignar un valor a la variable de la izquierda basado en el valor de la derecha
#El operador de asignación más utilizado es el igual (=), el cual asigna el valor que se encuentra de lado derecho a la variable de lado izquierdo
#Es decir, x = y asigna el valor de y a x.

#En python, contamos con los siguientes operadores de asginación:
#Asignacion: se implementa con ayuda del signo igual a (=), es el más simple de todos y asigna a la variable de lado izquierdo cualquier variable o valor de lado derecho 
# x = 5

#Asignación de resta: se implementa con la combinación de los signos -=, asigna en forma de resta a la variable de lado izquierdo, el valor de lado derecho
#  x = 8     x -= 5      (3)

#Asignación de multiplicación: se implementa con la cominación de los signos *=, asigna en forma de multiplicación a la variable de lado izquierdo, el valor de lado derecho.
#  x = 3        x *= 5      (15)

#Asignación de división: se implementa con la combinación de los signos /=, asigna en forma de división a la variable de lado izquierdo, el valor de lado derecho
#   x = 10      x /= 3      (3.3)

#Asignación de división entera: se implementa con la combinación de los signos //=, calcula y asigna la división entera a la variable de lado izquierdo, el valor de lado derecho.
#  x = 10       x //= 3 (3)

#Asignación de Exponente: se implementa con la combinación de los signos **=, calcula y asigna el exponente a la variable de lado izquierdo, el valor de lado derecho.
#   x = 2       x **= 5         (32)

#Asignación de Módulo o resto (%=): se implemente con la combinación de los signos %=, devuelve y asigna el resto o módulo de la división a la variable de lado izquierdo con el valor de lado derecho
#   x = 10      x %= 2          (10)


nombre = "Hola "
nombre += input("Escribe tu nombre: ")

print(nombre, ", esto es el incremento y decremento de una variable \n")

print("incremento o aumento: ")
x=1
print("El valor inicial de x es: ", x)
x += 1
x += 1
x += 1
x += 1
x += 1
print("El valor final de x es:", x, "\n")

print("decremento o disminución: ")
print("El valor inicial de x es: ", x)


x -= 1
x -= 1
x -= 1
x -= 1
x -= 1
print("El valor final de x es: ", x)