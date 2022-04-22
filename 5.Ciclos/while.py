#En ocasiones cuando estamos desarrollando un programa, nos encontramos con la necesidad de ejecutar una o más líneas de código en repetidas ocasiones, con lo cual la opción más lógica es duplicar el código de estas instrucciones para el que programa realice la tarea asignada
#Sin embargo, esta alternativa no es la más optima ya que duplicar código puede generar diversos problemas como, por ejemplo, archivos innecesariamente más extensos y dificiles de comprender al momento de querer realizar alguna modificación o actualización del mismo
#Ante esta situación, en programación contamos con sentencias de repetición de código, las cuales nos permiten ejecutar una serie de instrucciones o líneas de código de manera controlada dentro de nuestros programas, a las cuales se les conoce como ciclos o bucles
#Un ciclo o bucle permite ejecutar en repetidas ocasiones las instrucciones o líneas de código indicadas por el programador, con lo cual, no existe la necesidad de duplicar líneas de código para ejecutarlas en más de una ocasión
#En python contamos con el ciclo o bucle while, el cual permite repetir la ejecución de un grupo de instrucciones, mientras se cumpla una condición, es decir, mientras la condición del ciclo o bucle se cumpla las instrucciones se seguirán ejecutando 

#Ejemplo 1
x=1

while x < 3:
    print(x)
    x+=1

print("Fin.")

#Ejemplo 2
x = 0
while x < 1000:
    print("Hola")
    x+=1