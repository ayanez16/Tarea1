#En un almacén se hace un 20% de descuento a los clientes cuya compra supere
#los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
#pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
#necesario.
monto = int(input("Ingrese su valor a pagar: "))
descuento = 0
if monto > 1000:
    descuento = (monto*20) // 100
    pagar = monto - descuento
    print("Su valor final ha pagar es: " +str(pagar))
else:
    print("No obtiene descuento, por lo tanto su valor final ha pagar es: " + str(monto))
