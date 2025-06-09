# show inverted phrase

frase = input("Enter a phrase: ")
print(frase[::-1]) # beginning : end : salto

# show inverted phrase with WHILE

frase = input("Enter a phrase: ")
reversed_frase = ""
i = len(frase) - 1
print (i)

while i >= 0:
    reversed_frase += frase[i]
    i -= 1

print(reversed_frase) 

# show inverted phrase with BUCLE FOR

frase, t = input("Enter a phrase: ") , ""
for k in range(len(frase)-1,-1,-1):
    t += frase[k]
print(t)
