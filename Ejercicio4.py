#Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
a = int(input("Ingrese el valor a: "))
b = int(input("Ingrese el valor b: "))
c = int(input("Ingrese el valor c: "))
x1 = (-b + (((b**2) - (4*a*c))**0.5)) / (2*a)
x2 = (-b - (((b**2) - (4*a*c))**0.5)) / (2*a)
print("El valor de X1 es: " + str(x1))
print("El valor de X2 es: " + str(x2))