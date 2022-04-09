#Usamos las declaraciones para controlar  el flujo de nuestra aplicaciones
#Usualmente solo queremos que cierto codigo sea ejecutado cuando una condicion particular ocurra
#Por ejemplo, if mi perro tiene hambre (aplicar logica), else (aplicar logica si el perro no tiene hambre)

#Para controlar este flujo de logica usamos palabras clave:
#if 
#elif
#else

#Python usa un Sistema de indentación al momento que declaramos funciones y logica con if

#Se llama "Control Flow Syntax" y usamos: e indetacion (espacios en blanco)

#Este sistema de indentaciones muy importante y es lo que separa a python del resto de lenguajes 

#Declaracion If, Elif Y Else
#Sintacis de una declaracion IF
#   If alguna_condicion:
    #Ejecutamos codigo

#Sintaxis de una declaracion IF/ELSE
#   If alguna_condicion:
    #Ejecutamos codigo
#else:
    #Aplicar segunda codicion

#Sintaxis de una declaracion ELIF
# #If alguna_condicion:
#elif alguna_otra_condicion:
    #algo distinto
#else: 
    #hacer algo mas

print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cual es tu nombre?:")

matematicas = int(input(nombre + " ¿Cual es tu calificacion en matematicas?: ")) #Introduccion Calificacion
quimica = int(input(nombre + "¿Cuál es tu calificacion en Quimica?: "))
biologia = int(input(nombre + "¿Cual es tu calificacion en biologia?:  "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)
if promedio >= 6:
    print("Felicidades " + " " + nombre + "aprobaste con un promedio de: ", promedio)
print("Fin.")


hambre = True
sed = True

if hambre and not sed:
    print('Tenemos hambre!')
elif hambre == True and sed == True:
    print("Tenemos hambre y sed!")
else:
    print("Estamos llenos!")