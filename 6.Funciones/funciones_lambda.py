#Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas y anónimas (no es necesario proporcionar un nombre para las funciones lambda). Las funciones Lambda se comportan como funciones normales declaradas con la palabra clave def

numeros = [1,2,3,4,5]

def square(num):
    result = num**2
    return result

#for item in map(square, numeros):
#    print(item)

#Retornar los numeros en una lista al cuadrado

print(list(map(square, numeros)))


#Encontrar numeros pares
def check_even(num):
    return num%2 == 0

for n in filter(check_even, numeros):
    print(n)

#Funcion lambda
numeros = [1,2,3,4,5,6,7]

print(list(map(lambda num: num ** 2, numeros)))
print(list(filter(lambda num: num%2 == 0, numeros)))

name = 'Variable global'

def saludo():

    # Enclosing
    name = 'Ileana'

    def hola():

        # Local
        name = 'Variable Local'
        print('Hola ' + name)

    hola()
saludo()


x = 50

def func():
    global x
    print(f'X es {x}')
    #  Re Asignacion Local
    x = 'Nuevo Valor'
    print(f'Fui localmente cambiada de x a {x}')

func()
print(x)