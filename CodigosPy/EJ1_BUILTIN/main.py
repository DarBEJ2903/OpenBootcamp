import pprint

if __name__ == '__main__':

    int_usr = input("Ingrese una lista de paises separados por cóma: ") #INGRESO DE DATOS POR CONSOLA
    list_paises = int_usr.split(',')  # CONVIERTE LOS DATOS INGRESADOS Y SEPARADOS POR COMAS A UNA LISTA
    list_paises = map(lambda x: x.strip().capitalize(),list_paises) #ELIMINA ESPACIOS EN BLANCO DE CADA ELEMENTO DE LA LISTA Y COLOCA EN MAYUSCULA LA PRIMEA LETRA
    list_paises = set(list_paises) #ELIMINA LOS DATOS REDUNTANTES O REPETIDOS
    list_paises = list(list_paises)  # CONVIERTE EL CONJUNTO A UNA LISTA
    list_paises.sort()             # ORDENA LA LISTA ALFABETICAMENTE EN ORDEN ASCENDENTE
    
    for i in list_paises:          # IMPRIME POR CONSOLA LOS DATOS DE LA LISTA
        print(f'{i},\n')
