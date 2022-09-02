def crearFichero(Nombre_Fichero):
    f = open(Nombre_Fichero,'xt')

def escribirFichero(Nombre_Fichero):
    with open('Nombre_Fichero', 'w+',encoding='utf-8') as f:
        datos = input("Escribe algo en el fichero: ")
        f.write(datos)

def main():
    Nombre_Fichero = input('Nombre Fichero: ') + '.txt'
    crearFichero(Nombre_Fichero)
    print(f'Fichero {Nombre_Fichero} esta abierto')
    print("Escribiendo en fichero")
    f = escribirFichero(Nombre_Fichero)


if __name__ == '__main__':
    main()

