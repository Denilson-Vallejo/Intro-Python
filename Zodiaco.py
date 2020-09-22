dia = int(input("Ingresa el día de tu nacimeinto: "))
mes = int(input("Ingresa el número de mes de tu nacimiento: "))
mes = mes*100
dia = mes + dia

if (dia <122 and dia>100) or (dia > 1222 and dia < 1232):
    print("Eres capricornio.")
elif(dia <= 520 and dia >= 122):
    if (dia >= 122 and dia <=217):
        print("Eres acuario.")
    elif (dia > 217 and dia <=320):
        print("Eres piscis. ")
    elif (dia > 320 and dia <=419):
        print("Eres aries.")
    elif(dia > 419 and dia <=520):
        print("Eres tauro.")
    else:
        print("Eres Géminis")
else:
    if(dia>620 and dia<=722):
        print("Eres cáncer.")
    elif(dia>722 and dia<=822):
        print("Eres leo.")
    elif(dia>822 and dia <=922):
        print("Eres virgo")
    elif(dia>922 and dia <=1022):
        print("Eres libra")
    elif(dia>1022 and dia<=1121):
        print("Eres escorpio")
    else:
        print("Eres sagitario")
