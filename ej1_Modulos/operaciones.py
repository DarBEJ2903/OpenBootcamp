def sum():
    while True:
        try:
            args = input("INGRESE SUMANDOS: ")
            args = args.split('+')
            suma = 0
            args = [float(i) for i in args]
            for i in args:
                suma += i
            return suma
        except:
            print("Ingrese Valores Validos")

def resta():
    while True:
        try:
            resta = input("Ingrese Resta: ")
            resta = resta.split('-')
            resta = [float(i) for i in resta]
            return resta[0] - resta[1]
        except:
            print("Ingrese Valores Validos")

def multiplicar():
    while True:
        try:
            fact = input("INGRESE FACTORES: ")
            fact = fact.split('*')
            fact = [float(i) for i in fact]
            prod = 1
            for i in fact:
                prod = prod*i
            return prod
        except:
            print("INGRESE VALORES VALIDOS")


def dividir():
    while True:
        try:
            div = input("Ingrese Division: ")
            div = div.split('/')
            div = [float(i) for i in div]
            assert div[1] != 0
            return div[0]/div[1]
        except:
            print("INGRESE VALORES VALIDOS")

