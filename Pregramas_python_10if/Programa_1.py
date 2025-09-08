#PROGRAMA1
#CRISTOPHER_ALVAREZ_HERNANDEZ
bol=float(input("Ingresa el valor del boleto"))
edad=float(input("Ingresa tu edad"))
if (edad>=1)and(edad<=12):
    des=bol/2
    print("Tu total a pagar es",des)
if (edad>=13)and(edad<=17):
    des=bol*0.3
    tot=bol-des
    print("Tu total a pagar es",tot)
if (edad>=18)and(edad<=59):
    des=bol*0.2
    tot=bol-des
    print("Tu total a pagar es",tot)
if (edad>=60):
    print("Por tu edad el boleto es gratis")
    