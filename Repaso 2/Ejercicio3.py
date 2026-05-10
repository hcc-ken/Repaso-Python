palabra = input("Introduzca una frase.")
vocales = "aeiouAEIOU"
contador_vocales = 0

# se le asignará a i, lo que haya en palabra, como palabra es una cadena de string, por ejemplo, H o l a _ m u n d o. i = H, después o, después l....
for i in palabra:
    if i in vocales:
        contador_vocales += 1

print(contador_vocales)