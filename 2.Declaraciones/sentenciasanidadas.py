#Las sentencias condicionales anidadas, se presentan cuando por el camino de verdadero o falso de una sentencia condicional hay otra sentencia condicional
#Es decir, cuando trabajamos con sentencias condicionales simples, compuestas o múltiples, podemos colocar dentro de la instrucción o instrucciones a ejecutar de cada una de estas sentencias, otra sentencia condicional.
#En conclusión, las sentencias condicionales anidadas consisten en tener una instrucción condicional dentro de la otra, y dependiendo de si la condición de la primera sentencia condicional se cumple o no se cumple, se ejecutará otra sentencia condicional.

#De esta manera, tendremos una condición dentro de otra condición, ampliando la cantidad de opciones para que nuestros programas puedan resolver un problema, sin importar la cantidad de situaciones que se presenten.

#Menú de opciones:
#Presiona 1 para convertir de número a palabra
#Presiona 2 para convertir de palabra a número

#¿Cuál es tu opción deseada?: 
 
print("==========")
print("Conversor")
print("========= \n")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número. \n")

opcion = int(input("¿Cuál es tu opción deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra. \n")

    opcion_uno = int(input("¿Cual es el numero que deseas convertir a palabra? (1 - 5): "))
    
    if opcion_uno == 1:
        print("El número es 'UNO'")
    #Sentencia condicional anidadas
    elif opcion_uno == 2:
        print("El número es 'DOS'")
    elif opcion_uno == 3:
        print("El número es 'TRES'")
    elif opcion_uno == 4:
        print("El número es 'CUATRO'")
    elif opcion_uno == 5:
        print("El número es 'CINCO'")
    else: 
        print("El número seleccionado no esta registrado")
elif opcion == 2:
    print("\n Conversor de palabra a número. \n")
    
    opcion_dos = input("¿Cual es la palabra que deseas convertir a número?: ")

    if opcion_dos == "uno":
        print("El número es '1'")
    elif opcion_dos == "dos":
        print("El número es '2'")
    elif opcion_dos == "tres":
        print("El número es '3'")
    elif opcion_dos == "cuatro":
        print("El número es '4'")
    elif opcion_dos == "cinco":
        print("El número es '5'")
    else: 
        print("El número seleccionado no esta registrado.")
else:
    print("Opcion no disponible") 

print("Fin.")