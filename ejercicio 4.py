#Para un valor entero positivo que representa una cantidad en segundos, indicar
#su equivalente en minutos, horas y días.
segundos = int(input("Escriba la cantidad de segundos: "))
dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // 3600
segundos1 = segundos % 3600
minutos = segundos1 // 60
segundos2 = segundos1 % 60
print("Su equivalente de los segundos es: " + str(minutos) + " minutos , " + str(horas) + " horas y " + str(dias) + " dias")
#print("Minutos = " + str(minutos) + "")