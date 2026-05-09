# Códigos ANSI
RESET = "\033[0m"
NEGRITA = "\033[1m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"

# Eso es una funcion con un parámetro llamado color que puede ser cualquier cosa, en este caso los colores que están declarado encima.
def linea(color):
    print(color + "=" * 15 + RESET)

numero = int(input("Introduzca un número."))

# Llamamos a las variables de arriba que contienen los códigos ANSI (Códigos que python sabe interpretar como colores)
print(VERDE + f"Tabla del {numero}" + RESET)

linea(AZUL)

for i in range (1, 11):
    print(VERDE + f"{numero:>2} x {i:>2} = {numero * i}" + RESET)

linea(AZUL)