#En python, los operadores relaciones son símbolos que se usan para comparar dos valores, y generalmente son utilizados en las sentencias condicionales para la toma de decisiones.
#Al utilizar operadores relacionales dentro de una sentencia condicional, si el resultado de la comparación es correcto, la expresión o condición es considerada verdadera(true), y en caso contrario será falsa(false).
#Operador       Nombre       Ejemplo       Significado
#  <            Menor que   5 < 4           5 es menor que 4
#  >            Mayor que   7 > 5           7 es mayor que 5
#  ==           Igual a     5 == 5          5 es igual a 5
#  !=           No igual a (diferente) 4!=  4 no es igual a 5
#  <=           Menor que o igual a       6 <= 6        6 Es menor que o igual a 6
# >=            Mayor que o igual a        9 >= 5       9 Es mayor que o igual a 5


#Practica
print("Introduce dos numeros a comparar: \n")

num_uno = int(input("Introduce el primer número:  "))
num_dos = int(input("Introduce el segundo número: "))

print("\n Los números a comparar son: ", num_uno, " y ", num_dos, "\n")

if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("Es diferente...")
if num_uno < num_dos:
    print("Es menor...")
if num_uno > num_dos:
    print("Es mayor...")
if num_uno <= num_dos:
    print("Es menor o igual...")
if num_uno >= num_dos:
    print("Es mayor o igual...")
