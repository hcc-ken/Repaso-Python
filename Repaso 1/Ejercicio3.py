frase = input("Introduzca una frase.")
vocales = "aeiouAEIOU"
contador_de_vocales = 0

for i in frase:
    if i in vocales:
        contador_de_vocales += 1

palabras = frase.split()
contador_de_palabras = len(palabras)

frase_invertida = frase[::-1]

print(f"Vocales: {contador_de_vocales}")
print(f"Palabras: {contador_de_palabras}")
print(f"Frase invertida: {frase_invertida}")