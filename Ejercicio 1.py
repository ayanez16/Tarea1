#Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
#dicho número.
num = int(input("Porfavor, ingrese un numero: "))
contador = len(str(num))

print("El numero ingresado tiene "+str(contador) +" digitos")