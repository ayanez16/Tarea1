#Todos los años que se dividen exactamente entre 400, o que son divisibles
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
#Usando estas premisas crea un algoritmo que lea una fecha como un número
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
#el mismo es un año bisiesto o no.
fecha = int(input("Ingrese una fecha en formato ddmmaaaa: "))
año = fecha % 10000
dia= fecha // 1000000
mes= (fecha // 10000) % 100
# print(dia,"/",mes,"/",año)
if año % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")
