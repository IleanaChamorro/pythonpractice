#La compañia multinacional Rappi, solicita un sistema que determine los días de vacaciones a los que tiene derecho un trabajador, tomando en cuenta las siguientes características:
#Existen tres departamentos dentro de la compañia con sus respectivas claves:
#Departamento de Atención al cliente (clave 1)
#Departamento de Logística(clave 2)
#Gerencia (clave 3)

#Trabajadores con clave 1(Atención al cliente)
#Con 1 año de servicio, reciben 6 días de vacaciones
#Con 2 a 6 años de servicio, reciben 14 días de vacaciones
#A partir de 7 años de servicio, reciben 20 días de vacaciones

#Trabajadores con clave 2(Logística):
#Con 1 año de servicio, reciben 7 días de vacaciones
#Con 2 a 6 años de servicio, reciben 15 días de vacaciones
#A partir de 7 años de servicio, reciben 22 días de vacaciones

#Trabajadores con clave 3(Gerencia):
#Con 1 año de servicio, reciben 10 días de vacaciones
#Con 2 a 6 años de servicio, reciben 20 días de vacaciones
#A partir de 7 años de servicio, reciben 30 días de vacaciones

#Requerimientos indispensables:
#El sistema debe de solicitar el "Nombre", "Clave del departamento" y "Antiguedad" del trabajador desde teclado
#Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga el nombre del trabajador y los días de vacaciones a los que tiene derecho 


print("*******************************")
print("'Sistema de control vacacional Rappi'")
print("******************************* \n")

#Solicitud de Datos
nombre_empleado = input("Por favor introduce el nombre del empleado: ")
clave_departamento = int(input("Por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce los años laborados del empleado: "))

#Validacion clave departamento
if clave_departamento == 1:

    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, " tiene derecho a 6 días de vacaciones")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 14 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 20 días de vacaciones")
    else:
        print("El empleado", nombre_empleado, "aún no tiene derecho a vacaciones")

elif clave_departamento == 2:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, " tiene derecho a 7 días de vacaciones")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 15 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 22 días de vacaciones")
    else:
        print("El empleado", nombre_empleado, "aún no tiene derecho a vacaciones")
elif clave_departamento == 3:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, " tiene derecho a 10 días de vacaciones")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 20 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 30 días de vacaciones")
    else:
        print("El empleado", nombre_empleado, "aún no tiene derecho a vacaciones")
else:
    print("La clave de departamento no existe, vuelve a intentarlo. ")