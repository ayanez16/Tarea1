#Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
#decenas, centenas y unidades de mil.
numero = int(input("Ingrese un numero de 4 cifras: "))
unidades = numero % 10
decenas = (numero % 100 - numero % 10) // 10
centenas = (numero % 1000 - numero % 100) // 100
unimil = (numero % 10000 - numero % 1000) // 1000
print("Unidades: " + str(unidades))
print("Decenas: " + str(decenas))
print("Centenas: " + str(centenas))
print("Unidades de mil: " + str(unimil))
