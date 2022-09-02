"""
 Serializaciòn: Consiste en convertir un objeto o cualquier otra cosa a una secuencia de datos
                que pueda escribir en disco. Consiste en guardar la representacion de un programa
                a una secuencia de datos que se pueda escribir en un fichero.
                El modulo pickle nos permite esto
"""
import pickle

class Juguete():
    nombre = ""
    precio = 0.0
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def getNombre(self):
        return self.nombre

#j1 = Juguete("Balon de futbol",15000)
# Serializando el objeto j1 en un archivo 'datos.bin'
#f = open('datos.bin','wb')
#pickle.dump(j1,f)
#f.close()


## DESERIALIZANDO (LEER) EL ARCHIVO 'datos.bin' QUE CONTIENE LA REPRESENTACION DE UN OBJETO

f = open('datos.bin','rb')
juguete_balon = pickle.load(f)
f.close()
print(juguete_balon.getNombre(),juguete_balon.precio)
