RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"

# Creamos la funcion tarea y dentro del parámetro le introducimos la lista
def tarea(lista):
    # pedimos al usuario que introduzca un string
    nueva = input("Añada la tarea: ")
    #Append es como .add en java, añadir a la lista un elemento. (Lo que hay dentro del parámetro)
    lista.append(nueva)
    #Llamamos a la función, introduciendo en el parámetro el texto y el color que queremso
    mostrar_mensaje("Tarea añadida.", AZUL)

#Creamos funcion e introducimos la lista en el parámetro
def mostrar_tarea(lista):
    #Mostrar mensaje
    mostrar_mensaje("Lista de tareas.", VERDE)
    #Recorremos con un bucle for según la longitud de nuestra lista.
    for i in range (len(lista)):
        #Imprimimos la lista. i + 1 es porque si no, empezamos por el número 0, y no quermos eso. 
        print(f"{i + 1}. {lista[i]}")

def completar_tarea(lista):
    num = int(input("Introduzca el número de la tarea que desea completar: "))
    #Pop es eliminar, .remove. Hace falta -1 porque si no, eliminaremos la posición errónea de la lista ya que el programa cuenta a partir del 0, el usuaruio no. 
    lista.pop(num - 1)
    mostrar_mensaje("Borrado.", AMARILLO)

# Esto es una función que requiere un texto, cualquiera, y un color, cualquiera.
def mostrar_mensaje(texto, color):
    # El largo será la longitud del texto que introduzcamos en el parámetro.
    largo = len(texto)
    print(color + "-" * (largo + 2))
    print("| " + texto + " |")
    print("-" * (largo + 2) + RESET)

# Hay que declarar el array.
lista = []

# Bucle while para que se repita una y otra vez.
while True:
    print("1. Añadir tarea")
    print("2. Ver todas las tareas numeradas")
    print("3. Marcar tareas como completadas")
    print("4. Salir del programa")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        tarea(lista)
    elif opcion == "2":
        mostrar_tarea(lista)
    elif opcion == "3":
        completar_tarea(lista)
    elif opcion == "4":
        # Finalizamos el bucle con un break.
        break