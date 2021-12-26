#Dado un (1) número binario de cuatro (4) dígitos imprimir su valo
numbi = int(input("Ingresar un numero binario: "))
decimal = 0
i = 0
while (numbi > 0):
    digito = numbi % 10
    numbi = int(numbi//10)
    decimal = decimal + digito * (2**i)
    i = i + 1
print("El valor del numero ingresado es: " + str(decimal))