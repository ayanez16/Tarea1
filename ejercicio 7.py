#Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
#centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
#de IMC de la persona y la categoría en la cual fue clasificado.
peso = float(input("Ingrese el peso de la persona (lb): "))
estatura= float(input("Ingrese la estatura de la persona (cm): "))
pkg = peso/2.2046
pesokg = round(pkg,2)
estaturam = estatura/100
imc = pkg / estaturam ** 2
imcr = round(imc,2)
print("El peso de la persona es de: " + str(pesokg) + " kg")
print("El valor de la IMC de la persona es: " + str(imcr))
if imc < 16:
    print("Su categoria es: Criterio de ingreso")
elif imc >= 16 and imc <= 16.9:
    print("Su categoria es: Infra peso")
elif imc >= 17 and imc <= 18.4:
    print("Su categoria es: Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Su categoria es: Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Su categoria es: Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Su categoria es: Obesidad pre-morbida")
elif imc >= 40 and imc <= 45:
    print("Su categoria es: Obesidad morbida")
else:
    print("Su categoria es: Obesidad hiper-morbida")


