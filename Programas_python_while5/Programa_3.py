#PROGRAMA3
#CRISTOPHER_ALVAREZ_HERNANDEZ
num=0
prom=0
respuesta="x"
while (respuesta!="N")or(respuesta!="n"):
    cal=float(input("Ingresa calificacon: "))
    prom=prom+cal
    num=num+1
    respuesta=(input("Deseas continuar S o N"))
    if (respuesta=="n")or(respuesta=="N"):
        break
promf=prom/num
print("Tu promedio es",promf)