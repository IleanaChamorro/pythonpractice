#Coleccion Unica y Desordenada de Elementos
#Solamente puede Haber Una representacion del mismo objeto

miset = set() #Definiendo set

miset.add(2) #Agregado objeto
miset.add(3)
miset.add(2) #No se agrega al set, ya que solo se puede tener valores unicos

#Ver valores de lista repetidos
milista = [1,1,1,1,1,2,2,2,3,3,3]

print(set(milista))
