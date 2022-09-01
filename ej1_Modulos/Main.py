import operaciones
def main():
    suma = operaciones.sum()
    print(suma)
    res = operaciones.resta()
    print(res)
    prod = operaciones.multiplicar()
    print(prod)
    div = operaciones.dividir()
    print(div)

if __name__ == '__main__':
    main()