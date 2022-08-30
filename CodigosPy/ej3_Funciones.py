def yearBis(year):
    try:
        year = int(year)
        if year%4 == 0 and year%100 == 0 and year%400 == 0:
            print("EL AÑO ES BISCIESTO")
        elif year%4 == 0 and year%100 != 0:
            print("EL AÑO ES BISCIESTO")
        else:
            print("EL AÑO NO ES BISCIESTO")





    except:
        print("DATO INGRESADO NO VALIDO")
yearBis(input("INGRESA UN AÑO: "))