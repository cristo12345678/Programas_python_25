#PROGRAMA7
#CRISTOPHER_ALVAREZ_HERNANDEZ
pro=float(input("Ingresa el valor del producto"))
can=int(input("Ingresa la cantidad de productos comprados"))
total=can*pro
if (total>500):
    des=total*.20
    tot=total-des
    print("Tu total a pagar es",tot)
else:
    des=total*.10
    tot=total-des
    print("Tu total a pagar es",tot)