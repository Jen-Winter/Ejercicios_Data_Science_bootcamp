precio = input("Add the price in euros in the format 00.00: ")
EsDecimal = True
# SPLIT method
#precio_split = precio_euros.split(".")
#precio_entero = precio_split[0]
#precio_centimos = precio_split[1]


#print(f"El precio es {precio_entero} euros y {precio_centimos} centimos.")

# WHILE method
#precio_euros = ""
#precio_centimos = ""
#k, K = 0 , 0

#while k < len(precio):
#    if precio[k] == "." or precio[k] == ",":
#        EsDecimal = False
#    elif EsDecimal:
#            precio_euros += precio[k]
#    else:
#        if K<2:
#            precio_centimos += precio[k]
#            K+=1
#    k+=1

#print(f"El precio es {precio_euros} euros y {precio_centimos} centimos.")
#print(precio_euros,precio_centimos,sep=",")

# FOR method

precio_euros = ""
precio_centimos = ""
K = 0
EsDecimal = False

for k in precio:
    if k == "." or k == ",":
        EsDecimal = True
    else:
        if EsDecimal == False:
            precio_euros += k
        else:
            if K < 2:
                precio_centimos += k
                K += 1

print(precio_euros,precio_centimos,sep=",")