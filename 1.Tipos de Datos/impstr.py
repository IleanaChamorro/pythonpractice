#Usualmente queremos "inyectar" una variable en una cadena para imprimir
#Por ejemplo:
#mi_nombre = "Eric"
#Print("Hola" + mi_nombre)


#Hay multiples maneras de formatear cadenas para imprimir variables en ellas
#A esto se le dice "interpolacion de cadenas"

print('Esta es una cadena de {}'.format('TEXTO'))
print('Esta {0} {1} {2}'.format('es', 'una', 'cadena'))
print('Esta {e} {u} {c}'.format(e='es', u='una',c='cadena'))

resultados = 100/888
print("Los resultados son {}".format(resultados))

#Formateo de float "{valor:width.precision f}"
print("Los resultados son {r:1.3f}".format(r=resultados))

nombre = "Ileana"
edad = 18

print(f"Los desarrolladores son {nombre} con edad de {edad}")