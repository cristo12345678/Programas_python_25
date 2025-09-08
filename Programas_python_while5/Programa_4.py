#PROGRAMA4
#CRISTOPHER_ALVAREZ_HERNANDEZ
respuesta="x"
while (respuesta!="N")or(respuesta!="n"):
    num=float(input("Ingresa un numero: "))
    resul=num*2
    print("El doble del numero es: ",resul)
    respuesta=(input("Deseas continuar S o N"))
    if (respuesta=="n")or(respuesta=="N"):
        break
print("Programa terminado")