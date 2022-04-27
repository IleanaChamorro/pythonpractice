#Sentencias break y continue
#Para lograr la interrupción de una iteración, contamos con las sentencias break y continue.
#En python, la sentencia break se utiliza para detener la ejecución de una iteración y salir de ella, con lo cual, el programa podrá continuar con la ejecución del código que se encuentre fuera de nuestro bucle

#Ejemplo para break
print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("Valor actual de la variable: ", contador)

print("Fin del programa, la sentencia break se ha ejecutado")

#Ejemplo para continue

print("\n while con la sentencia continue \n")
contador = 0

while contador < 10:
    contador += 1 

    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)