#Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
cateto1  =  int(input("Introducir el valor del cateto 1: " ))
cateto2  =  int(input("Introducir el valor del cateto 2: " ))
hipotenusa = (cateto1**2 + cateto2**2)**.5
print("El valor de la hipotenusa es: " + str(hipotenusa))