def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal

def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinal = ''

    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chrd(ascii)
    return textoFinal
     
def encriptarArchivo(rutaArchivo):
    #Creación archivo
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    #Encriptación texto
    textoEncriptado = encriptar(texto)

    #Abrir archivo y escribirlo
    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo se encriptó correctamente')

def desencriptarArchivo():
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('El archivo se desencriptó correctamente')

respuestaEoD = input('Presione "E" para encriptar, o "D" para desencriptar: ')
rutaArchivo = input('Ingrese la ruta del archivo: ')


if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)