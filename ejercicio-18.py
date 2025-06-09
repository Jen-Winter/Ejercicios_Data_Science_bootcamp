frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal :")
vocal = vocal.lower()

#muestre por pantalla la frase pero con la vocal introducida en mayuscula

#PLUS + method

#frase_modificada = frase + " " + vocal.capitalize()
#print(frase_modificada)

#JOIN method .join()

#frase_modificada_join = " ".join([frase,vocal.capitalize()])
#print(frase_modificada_join)

#BUCLE FOR (for loop)

frase_modificada = ""

#for letra in frase:
#    if letra == vocal:
#        frase_modificada += letra.upper()
#    else:
#        frase_modificada += letra

#print(frase_modificada)

#BUCLE WHILE (while loop)

i = 0 #index

while i < len(frase):
    letra = frase[i]
    if letra == vocal:
        frase_modificada += letra.upper()
    else:
        frase_modificada += letra
    i += 1 #move to the next index, otherwise it gets stuck in the index [0]

print(frase_modificada)

