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