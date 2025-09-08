#PROGRAMA2
#CRISTOPHER_ALVAREZ_HERNANDEZ
respuesta="x"
while (respuesta!="N")or(respuesta!="n"):
    ciudad=input("Ingresa la ciudad: ")
    print("La ciudad es: ",ciudad)
    respuesta=(input("Deseas continuar S o N"))
    if (respuesta=="n")or(respuesta=="N"):
        break
print("Programa terminado")