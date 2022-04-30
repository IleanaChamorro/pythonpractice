arreglo = ['banana', 'melon', 'sandia', 'pera']

#for fruta in arreglo:
#    #Determinar todas las frutas que terminan en a
#    if fruta.endswith("a"): 
#        print("La fruta es: "+ fruta)

arreglo.reverse()
arreglo.remove("melon")
arreglo.append("kiwi")
for fruta in arreglo:
    if fruta == 'sandia':
        break
    print("la fruta es: " + fruta)


texto = "Hola mundo"

for letra in texto:
    print("Letra: "+ letra)

for numero in range(10):
    if(numero > 5):
        print(numero)