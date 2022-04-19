#Desarrollar una calculadora con las siguientes características:
#1. La calculadora deberá ser capaz de calcular las operaciones de suma, resta, multiplicación, división, división entera, exponente y módulo o resto
#2. La calculadora deberá tener un menú de opciones donde el usuario pueda elegir cual es la operación que desea ejecutar 
#3. La calculadora deberá solicitar únicamente dos valores por cada operación

#Requerimientos indispensables:
#El código de este programa deberá funcionar con única variable que se llamará número, es decir, no se permite la implementación de otra variable


print("Calculadora con una sola variable \n")

print("*****************")
print("* Menú de opciones *")
print("*****************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7 Modulo o resto \n")

numero = int(input("Introduce la opción deseada: "))

if numero == 1:
    print("Elegiste suma \n")
    numero = int(input("Introduce el primer número"))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es:", numero)

elif numero == 2:
    print("Elegiste resta \n")
    numero = int(input("Introduce el primer número"))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es:", numero)

elif numero == 3:
    print("Elegiste multiplicacion \n")
    numero = int(input("Introduce el primer número"))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es:", numero)

elif numero == 4:
    print("Elegiste division \n")
    numero = float(input("Introduce el primer número"))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la division es:", round(numero, 2))

elif numero == 5:
    print("Elegiste division entera \n")
    numero = int(input("Introduce el primer número"))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la division entera es:", numero)

elif numero == 6:
    print("Elegiste exponente \n")
    numero = int(input("Introduce el primer número"))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es:", numero)