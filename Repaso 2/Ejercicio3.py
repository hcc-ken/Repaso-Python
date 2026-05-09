palabra = input("Introduzca una frase.")
vocales = "aeiouAEIOU"
contador_vocales = 0

for i in palabra:
    if i in vocales:
        contador_vocales += 1

print(contador_vocales)