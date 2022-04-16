#Desarrollar un programa que solicite tres números enteros desde teclado al usuario, posteriormente, el programa deberá determinar e indicar a través de un mensaje en pantalla, cual de los tres números es el más grande

#Requerimientos indispensables:
#El mensaje en pantalla deberá mostrar el número que resulto ser el más grande de los tres, por ejemplo: 
#"El número 10 es el número más grande de los tres"

print("********************")
print("* Programa para determinar ¿Cuál es el número más grande de tres números? *")
print("********************")


num_uno = int(input("Introduce el primer número:  "))
num_dos = int(input("Introduce el segundo número:  "))
num_tres = int(input("Introduce el tercer número:  "))

if num_uno > num_dos and num_uno > num_tres:
    print("El número ", num_uno, " es el número más grande de los tres")
else: 
    if num_dos > num_tres:
        print("El número ", num_dos, " es el número más grande de los tres")
    else:
            print("El número ", num_tres, " es el número más grande de los tres")