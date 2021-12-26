#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
#resultado su equivalente en segundos.

horas = int(input("Ingrese una hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = ((horas * 60 * 60) + (minutos * 60))
print("El equivalente ha segundos es: " + str(segundos))