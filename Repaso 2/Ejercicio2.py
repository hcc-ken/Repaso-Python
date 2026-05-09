try:
    num = -1
    while num != 0:
        num = int(input("Introduzca un número: (0 para salir del programa)"))
        suma = 0
        for i in range(num + 1):
            suma += i
        print(suma)
except ValueError:
    print("El numero debe de ser un entero.")