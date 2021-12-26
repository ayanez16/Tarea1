#Dado un número N determinar si es un número primo.
numero = int(input("Ingrese un numero: "))
contador = 0
for i in range(1, numero+1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print("Es primo")
else:
    print("No es primo")