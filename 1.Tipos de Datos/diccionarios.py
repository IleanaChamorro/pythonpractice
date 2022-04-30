#Mapeos desordenados para guardar objetos
#Los diccionarios utilizan un orden basado en par clave/valor
#Este par clave/valor permite al usuario agarrar objetos sin necesidad de saber la locacion(numero) del indice
#Diccionarios usan brackets {} y : para simbolizar las llaves y su valor asociado

#Cuando deberiamos escoger una lista o un diccionario?
#Diccionarios: Objetos retornados por llave
#Desordenado y no se guarda, bueno para cuando no sabes donde se encuentra algo

#Listas: Objetos retornados por locacion
#Puede ser indice o slicing

mi_diccionario = {'panchos': '100', 'hamburguesa':'200', 'juguito':['manzana', 'banana']}
mi_diccionario['gaseosa'] = 300

print(mi_diccionario)
print(mi_diccionario['juguito'])
print(mi_diccionario['juguito'][1].upper())
print(mi_diccionario.keys())
print(mi_diccionario.items())


diccionario = {
    "Programar": "Programar es transformar el cafe en código",
    "POO": "Programación Orientada a Objetos",
    "MVC": "Modelo Vista Controlador"
}
print(diccionario["POO"])

numeros = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
}

texto = input("Ingrese un número: ")

textoFinal = ' '

for letra in texto:
    textoFinal += numeros[letra] + ' '
    
print(textoFinal)