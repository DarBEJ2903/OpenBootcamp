def numPrimos(num):
    try:
        num = int(num)
        for i in range(2,num):
            if num%i == 0:
                print("EL NUMERO NO ES PRIMO")
                break
        else:
            print("EL NUMERO ES PRIMO")

    except:
        print("VALOR INGRESADO NO VALIDO")

numPrimos(input("INGRESE UN NUMERO ENTERO: "))