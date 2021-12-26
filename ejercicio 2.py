#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es
#capicúa.
numero = int(input("Ingrese un numero de 5 cifras: "))
if str(numero) == str(numero)[:: -1]:
    print("El numero ingresado es capicua")
else:
    print("El numero ingresado no es capicua")