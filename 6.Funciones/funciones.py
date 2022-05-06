#Crear código limpio, ordenado y repetible es muy importante para nosotros ser efectivos programando

#Funciones:
#Nos permiten crear bloques de codigo que podemos ejecutar varias veces, sin necesidad de reescribir codigo redundate

#Crear funciones requiere de una sintaxis especial, empezamos con def
#Veamos un ejemplo:
#   def nombre_de_funcion(nombre):
#   #Corremos codigo
#   print("Las funciones retornan algo" + nombre)

#Tipicamente usamos la palabra clave return para retornar el valor de una funcion
#Return nos permite asignar un output de la function
#Funcion de suma:
#   def suma(num1, num2):
#       return num1+num2


def decir_hola(nombre):
    print('hola')
    print('¿como estas?' + nombre)

decir_hola('Ileana')

def suma(num1,num2):
    total = num1 + num2
    print(total)

suma(2,3)

#Saber si un numero es par en una lista
def chequear_numero(num_list):
    for number in num_list:
        if number % 2 == 0:
            print('True')
            return True
        else:
            pass
    print('False')
    return False
chequear_numero([1,3,5])