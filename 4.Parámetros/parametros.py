#Los parámetros sep y end

#La función print(), es quizás una de las herramientas más útiles en el lenguaje de programación Python, al momento de interactuar con los usuarios de nuestros programas.
#Por tal motivo, es indispensable conocer la manera en que podemos manipular dichas impresiones en pantalla, con la finalidad de tener el control completo del texto a mostrar. 

#El parámetro end, se utiliza para agregar cualquier cadena de caracteres al final de la salida e impresión en pantalla de la función print().
#Además, por defecto la función print() genera un salto de línea al terminar su ejecución, sin embargo, con ayuda del parámetro end, es posible evitar este salto de línea.


#Ejemplo para el parametro end
print("Esto es un", end="-*/")
print("ejemplo")

#Parámetro sep 
#En ocasiones, es posible que deseemos imprimir múltiples valores de manera legible utilizando la función print().
#El parámetro sep, se utiliza para dar formato a las cadenas de caracteres que deben imprimirse en pantalla, agregando un separador entre las cadenas que se imprimirán.

#Ejemplo para el parametro sep
print("1", "2", "3", "4", "5", sep="-")
