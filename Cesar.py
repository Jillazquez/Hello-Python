# Programa que con un texto y un numero aleatorio encripta la frase en clave cesar
import random

frase = input("Texto para enciptar en cesar\n")
frasefinal=""
numeromov = random.randint(1, 26)
print(numeromov)
frase = frase.upper()

for caracter in frase:
    if ((ord(caracter) + numeromov) > 91):
        frasefinal += chr(ord(caracter)-(26-numeromov))
    else:
        frasefinal += chr(ord(caracter)+numeromov)


print(frasefinal)