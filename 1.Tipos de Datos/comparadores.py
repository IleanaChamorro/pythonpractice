# == : Si los valores de dos operando son iguales, la condicion es verdadera : (a == b) NO es verdadero
# != Valores de dos operandos no son iguales, condicion es igual ; (a != b) es Verdadero 
# > Si los valores del operando izquierdo son mayores que el de la derecha entonces la condicion es verdadera ; (1 > 2) no es verdadero
# < Si el valor de operando izquierdo es mayor o igual que el de la derecha entonces es verdadero  ; (a >= b) no es verdadero
# >= Si el valor del operando izquierdo es mayor o igual que el de la derecha entonces es verdadero ; (a >= b) no es verdadero
# <= Si el operando izquierdo es menor que el derecho entonces condicion es verdadera ; (a <= b) es verdadero

#Podemos usar operadores logicos para combinar comparaciones
#And, Or, Not

1 < 2 #True
1 < 2 > 3 #True
1 < 2 and 2 < 3 #True
'y' == 'y' and 2 == 2 #True
'y' == 'y' or 3 == 2 #True
not 1 == 1 #False
300 > 6000 #False
not 300 > 6000 #True