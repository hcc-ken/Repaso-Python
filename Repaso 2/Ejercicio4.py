numero = -1

try:
    while numero != 0:
        print("1. Contar letras")
        print("2. Contar palabras")
        print("3. Invertir texto")
        print("4. Salir")

        numero = int(input("Introduzca número."))

        if numero == 1:
            letra = input("Introduzca una palabra.")
            letras = len(letra)
            print(f"Hay {letras} letras en {letra}")
        elif numero == 2:
            palabra = input("Introduzca una frase.").split(" ")
            palabras = len(palabra)
            print(f"Hay {palabras} palabras en la frase {palabra}")
        elif numero == 3:
            palabra = input("Introduzca una frase.")
            invertida = ""

            for i in palabra:
                invertida = i + invertida
            print(invertida)
        elif numero == 4:
            break


except ValueError:
    print("Error: Debe de ser un número")