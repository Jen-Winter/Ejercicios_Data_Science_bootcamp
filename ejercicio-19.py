email = input("Your email address: ")

# SPLIT METHOD
#email_split = email.split("@")
#print(f"{email_split[0]}@ceu.es")

# WHILE METHOD

new_email = ""

#while email[i] != "@": #keep looping UNTIL reach
#    new_email += email[i]
#    i += 1

#new_email += "@ceu.es"

#print(new_email)


# WHILE METHOD profe

direccion, Direccion, verificacion = "josecarlos@ironhack.com" , "" , True
letra = 0

while letra < len(direccion):
    if direccion[letra] == '@' and verificacion == True:
        Direccion += "@ceu.es"
        verificacion = False
    else:
        if verificacion == True:
            Direccion += direccion[letra]
    letra+=1

print(Direccion)

# FOR METHOD

k = 0
for k in email:
    if k == "@":
        new_email += "@ceu.es"
        break
    else:
        new_email += k
print(new_email)