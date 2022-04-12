#En ocasiones, es necesario utilizar más de dos condiciones lógicas dentro de una misma condición, con lo cual, nos vemos en la necesidad de implementar múltiples operadores relacionales para crear una expresión lógica mucho más compleja.
#Sin embargo, no es posible colocar dos condiciones lógicas dentro de una misma condición, sin el apoyo de algún elemento que les indique a nuestros programas, que se realizará la unión de dos o más condiciones lógicas dentro de una misma expresión.
#Para este tipo de situaciones existen los operadores lógicos, los cuales, permiten agrupar condiciones lógicas dentro de una misma condición. Es decir, con los operadores lógicos tenemos la posibilidad de utilizar múltiples operadores relaciones dentro de una misma condición lógica

#En python, contamos con tres tipos de operadores lógicos

#Operador Logico    Símbolo
#Conjunción         And
#Disyunción         Or
#Negación           not


#Ejemplo operador and
#if num_uno == 5 and num_dos >= 5:
#    print("Ambas condiciones se han cumplido. ")
#else:
#    print("Una o ambas condiciones no se han cumplido")

#Ejemplo operador or
#if num_uno == 5 or num_dos >= 5:
#    print("Una o ambas condiciones se han cumplido.")
#else:
#    print("Ninguna condición se ha cumplido. ")

#Ejemplo operador not
#if not num_dos > 5:
#    print("La condición se invirtió y se cumple al ser un número menor o igual a 5")
#else:
#    print("No se cumple la condición porque el número es mayor a 5")



#Practica

#Conjución
print("Conjunción (and)")

num_uno = int(input("Escribe un número mayor a 2 y menor a 5:"))

if num_uno > 2 and num_uno < 5:
    print("El número ", num_uno, " cumple con la condición. \n")
else:
    print("El número ", num_uno, " NO cumple con la condición. \n")

#Disyunción
print("Disyunción (or) ")

palabra = input("Para cumplir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido. \n")
else:
    print("La condición NO se ha cumplido.\n")

#Negación
print("Negación (not)")

num_uno = int(input("Introduce un número igual a 5: "))

if not num_uno == 5:
    print("\n  El número es diferente de cinco y SI cumple la condición. \n")
else:
    print("\n. El número es igual a cinco y NO cumple la condición. \n")
