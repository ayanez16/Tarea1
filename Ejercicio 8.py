#Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
#del 1 hasta la del 10.
numero = int(input("Ingrese el numero de la tabla que desea presentar: "))
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')
