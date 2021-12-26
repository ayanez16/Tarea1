#Dado un número entero N que representa una contraseña y asumiendo que una
#contraseña debe tener al menos 10 dígitos para ser segura, determine si la
#contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
#nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
#mostrar un mensaje de éxito al usuario, por salida estándar.
contraseña = int(input("Ingrese una contarseña de solo numeros de 10 digitos: "))
if len(str(contraseña)) >= 10:
    print("La contraseña ingresada es un exito")
else:
    print("Error contraseña solo de 10 digitos, ingrese nuevamente")