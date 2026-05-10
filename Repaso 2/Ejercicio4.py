def contador_letra():
    letra = input("Introduzca una palabra.")
    letras = len(letra)
    print(f"Hay {letras} letras en {letra}")

def contador_palabra():
    palabra = input("Introduzca una frase.").split(" ")
    palabras = len(palabra)
    print(f"Hay {palabras} palabras en la frase {palabra}")

def frase_invertida():
    palabra = input("Introduzca una frase.")
    invertida = ""

    for i in palabra:
        invertida = i + invertida
    print(invertida)

numero = -1
try:
    while numero != 0:
        print("1. Contar letras")
        print("2. Contar palabras")
        print("3. Invertir texto")
        print("4. Salir")

        numero = int(input("Introduzca número."))

        if numero == 1:
            contador_letra()
        elif numero == 2:
            contador_palabra
        elif numero == 3:
            frase_invertida()
        elif numero == 4:
            break


except ValueError:
    print("Error: Debe de ser un número")