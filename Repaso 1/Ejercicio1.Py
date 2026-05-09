# Le pedimos al usuario que introduzca un número y especificamos que sea un número entero
numero = int(input("Introduzca un número."))

# Imprimimos por 15 veces "="
print("=" * 15)

#Entramos en un bucle desde el 1 hasta el 11 sin contar el 11 (10 en total)
for i in range (1, 11):
    #:>2 es para darle 2 espacios a la derecha
    print(f"{numero:>2} x {i:>2} = {numero * i}")

print("=" * 15)