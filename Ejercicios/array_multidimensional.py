lat = 34.5
lon = 45.6
posicion = [lat, lon]

#Movimientos Rover
historial = [
    [34.5, 45.6, "2022/02/02 17:20:24"],
    [34.5, 45.3, "2022/02/02 17:20:34"],
    [35.5, 47.6, "2022/02/02 17:20:44"],
    [35.5, 47.6, "2022/02/02 17:20:54"],
    [34.5, 48.6, "2022/02/02 17:21:04"],
    [33.5, 49.3, "2022/02/02 17:21:14"],
]
indiceLongitud = 0
indiceLatitud = 1
indiceFecha = 2

for coordenada in historial:
    print(coordenada[indiceLongitud])