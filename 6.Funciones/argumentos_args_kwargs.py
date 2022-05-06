#El principal uso de *args y **kwargs es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción.

#def func(a,b):
#    #retornar el %5 de la suma de a y b 
#    return sum((a,b)) * 0.05
#
#func(40,50)

#Funciones con uso de args la cual retorna una tupla
def func(*args):
    return print(sum(args) * 0.05)

func(4,5,6,7,2,3,423,4,432424)



#Funcion con uso de kwargs, la cual retorna un diccionario
def funct(**kwargs):
    if 'fruit' in kwargs:
        print('Mi fruta escogida es {}'.format(kwargs['fruit']))
    else:
        print('no hay fruta')

funct(fruit='manzana', veggie='lechuga')

#Funcion con uso de args y kwargs
def funcion(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Me gustaria {}  {}'.format(args[0], kwargs['comida']))

funcion(10,30,50,animal='perro', comida='leche')