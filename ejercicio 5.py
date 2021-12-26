#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
#mayor? y ¿cuál es el segundo mayor?
A = int(input("Ingrese el primer numero: "))
B = int(input("Ingrese el segundo numero: "))
C = int(input("Ingrese el tercer numero: "))
while A > B and A > C:
    if B < A > C:
        print("El primer numero mayor es: "+ str(A))
    elif A < B > C:
        print("El primer numero mayor es: "+ str(B))
    elif A < C > B:
        print("El primer numero mayor es: "+ str(C))
# if B < A > C:
#     print("El primer numero mayor es: "+ str(A))
# elif A < B > C:
#     print("El primer numero mayor es: "+ str(B))
# elif A < C > B:
#     print("El primer numero mayor es: "+ str(C))
