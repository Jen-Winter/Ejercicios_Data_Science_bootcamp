fecha_nascimiento = input("Please add your birthdate in the format dd/mm/aaaa:")
i, d, m, a, part = 0, "", "", "" , 0
#WHILE

while i < len(fecha_nascimiento):
    if fecha_nascimiento[i] == "/":
        part +=1 #moves to the next part
    else:
        if part == 0:
            d += fecha_nascimiento[i]
        elif part == 1:
            m += fecha_nascimiento[i]
        else:
            a += fecha_nascimiento[i]
    i += 1

if d != 2:
    d = "0" + d
if m != 2:
    m = "0" + m

print(d,m,a,sep="/")

#WHILE metodo profe

f = "05-09-1986"
d , m , a =  "", "" , ""
pb ,sb = False , False
k = 0
while k < len(f):
    if (f[k] == "/" or f[k] == "-") and pb == False:
        pb = True
    else:
        if (f[k] != "/" or f[k] != "-") and pb == False:
            d += f[k]
            print("d",d)
        elif (f[k] == "/" or f[k] == "-") and pb == True:
            sb = True
        elif (f[k] != "/" or f[k] != "-") and pb == True and sb == False:
            m += f[k]
            print("m",m)
        else:
            a += f[k]
            print("a",a)
    k+=1