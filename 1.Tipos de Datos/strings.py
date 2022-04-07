#Las cadenas son secuencias de caracteres, usan sintaxis con comillas singulares o doble comillas
# 'hola' , "hola"
#Caracter: "cadena de texto con muchos caracteres"
#Indice: 0 1 2 3 4 5
#Indice Inverso: 0 -5 -4 -2 -1

#Debido a que las cadenas son secuencias ordenadas significa que Podemos usar indexado y slicing para agarrar sub-secciones de una cadena
#Notacion de indexado: [], asignado despues de la cadena
#Indexado te permite agarrar un caracter singular de una cadena de texto

#Slicing permite agarrar una sub-seccion de multiples caracteres, un "slice" de una cadena
#Tiene la siguiente sintaxis:
# [start:stop:step] -> [0:4:2] 
# Start es un indice numeric para el slice iniciar
# Stop es el numero donde paramos el slice
# Step son los pasos que damos

print("Hola")
print("hola \n mundo")
print(len("longitud"))


micadena = "hola mundo"

#Indexado
print(micadena[3])

#Slicing
mi_cadena = "prueba cadena"

#print(mi_cadena[start:stop:step])
print(mi_cadena[2:4:2])

#Slicing desde inicio hasta el final
print(mi_cadena[::])

#Propiedades y Metodos de Cadenas

name = "Ile"
#name[0] = 'S' Esto da error, ya que las cadenas son inmutables
ultimas_letras = name[1:]

print('I' + ultimas_letras)

letra = 'z'
letra = letra * 10

print(letra)

suma = '1' + '3'

print(suma)

x = 'hola mundo'
x = x.upper()
print(x)

y = 'HOLA MUNDO'
y = y.lower()
print(y)

#Separado por espacios
a = 'separado'
a = a.split('o')

print(a)