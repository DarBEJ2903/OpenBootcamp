"""
    Leer o escribir en Archivos: Para trabajar con Ficheros se hace instanciando la clase 'open'.
    Esta clase recibe 2 parametros ('ruta_del_archivo', 'r')
    la letra 'r' (segundo parametro), significa que el archivo solo puede ser leido. Este parametro puede ser:
    r-> Read
    w-> Write (Modifica totalmente el archivo)
    append -> Se agregara elementos adicionales al archivo
    x -> Create (se creara un archivo nuevo)

    t -> texto (para archivos planos de solo texto)
    b -> binary (para archivos planos de contenido binario)

    + -> plus
"""
def leerFichero():
    # LEYENDO UN FICHERO
    f = open('archivo1.txt','r')
    datos = f.read()
    #Para leer datos en una lista se hace con el metodo 'readlines()'
    f.close()
    print(datos)


def escribirFichero(nameFile , datos):
    ## Escribien en un archivo txt una lista de datos agregandole el salto de linea '\n' al final

    f = open(nameFile, 'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n'
        f.write(linea)
    f.close()

if __name__ == '__main__':
    leerFichero()
    lista = ['numero1' , 'numero2 ',  'numero3']
    escribirFichero('archivoCreado',lista)