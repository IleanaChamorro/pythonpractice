#Elige tu propia aventura


#Aventuras para elegir según el usuario
paginas = [
    "Página 1 0) Al principio pensé que era algún camión pasando a gran velocidad,\n pero el temblor se sostubo... Me desperte de golpe y pensé -ES UN TEMBLOR!... \nQué vas a hacer?\n1) Esperar a que pase\n2) Salir corriendo afuera\n3) Pedir ayuda",
    "Página 1) Me quede inmóvil, esperando a que el temblor pase...\n De repente se hizo la oscuridad... \nHubo mucho ruido... Sentí que algo se caía... \nFIN",
    "Página 2) Salí corriendo por las escaleras... de repente se apagaron todas \nlas luces y la puerta no habría... \nQué vas a hacer?\n4) Intentar romper la puerta\n3) Esconderme en el baño\n5) Saltar por la ventana",
    "Página 3) Me quede inmóvil, esperando a que el temblor pase... \nDe repente se hizo la oscuridad... \nHubo mucho ruido... Sentí que algo se caía... \nFIN",
    "Página 4) Le dí varias patadas a la puerta, pero esta no caía... \nHasta sentí que toda la casa se derrumbaba... FIN",
    "Página 5) Salté por la ventana... Había mucha gente en la calle, \nví como mi casa se derrumbaba... Esperamos a que el temblor pase... Esperamos horas, hasta días, y el temblor seguía... Continuara..."
]

def mostrarPagina(numpagina):
    #Mostrar texto elegido según numero
    texto = paginas[numpagina]
    print(texto)

    #Elección de página
    respuesta = input()
    mostrarPagina(int(respuesta))

mostrarPagina(0)