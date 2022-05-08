#Errores y Excepciones

#Eventualmente algo en nuestro codigo se va a romper, sobretodo si le damos el codigo a alguien mas para que use el programa y no pre vemos el posible escenario de uso
#Podemos usar manejo de errores para poder planear posibles casos de uso donde ocurra un error

#Usamos las palabras claves:

#Try: Esto bloquea el codigo de ser corrido (puede dar error)

#Except: Bloque de codigo es ejecutado en caso de haber un error en el bloque try

#Finally: Bloque de codigo ejecutado finalmente sin importar el error

try:
    #Intentamos correr este codigo
    #Puede haber errores
    resultado = 10 + '10'
    print(resultado)
except:
    print('Parece que hay un error, escribe correctamente las variables')