#PROGRAMA8
#CRISTOPHER_ALVAREZ_HERNANDEZ
tur=int(input("Ingresa turnos trabajados"))
pagtur=float(input("Ingresa cuanto te pagan por turno"))
pagsem=tur*pagtur
ture=(input("Trabajaste turnos extra SI o NO"))
if (ture=="SI") or (ture=="si"):
    turex=int(input("Ingresa turnos extra trabajados"))
    pagext=float(input("Ingresa cuanto te pagan por turno extra"))
    pagex=turex*pagext
    total=pagsem+pagex
    print("Tu pago semanal es",total)
if (ture=="NO"):
    print("Tu pago semanal es",pagsem)