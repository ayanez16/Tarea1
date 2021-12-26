#Construya un programa que dado un valor entero N, haga el cálculo de la función
#factorial utilizando estructuras iterativas.
numero = int(input("Ingrese un numero: "))
if numero>=1:
    f=numero
    while numero>=2:
        numero = numero-1
        f=f*(numero)
    print("el factorial es: ",f)
if numero==0:
    print("el factorial es 1")