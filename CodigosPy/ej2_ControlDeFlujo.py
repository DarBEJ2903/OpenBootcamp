numInicio = input("Escribe el numero de inicio: ");
numFinal = input("Escribe el numero final: ");

try:
    for index in range(int(numInicio),int(numFinal) + 1):
        if index % 2 == 1:
            print(index)

except ValueError:
    print("Valores Ingresados No Validos")