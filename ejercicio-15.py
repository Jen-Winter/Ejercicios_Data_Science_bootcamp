nombre = input("Introduce tu nombre: ")
nombre_mayus = nombre.upper()
longitud = len(nombre.replace(" ", ""))  # Excluye espacios

print(f"{nombre_mayus} tiene {longitud} letras")

