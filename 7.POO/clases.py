class Perro():
    def __init__(self,raza,nombre,puntos):
        #Atributos
        self.raza = raza
        self.nombre = nombre

        #Esperamos valor booleano Verdadero/Falso
        self.puntos = puntos

pitbull = Perro(raza='Pitbull', nombre='Sam', puntos=False)