import pickle

class Vehiculo:

    motor = None
    n_puertas = None
    color = None
    fabricante = None

    def __init__(self,**kwargs):  #Constructor de la clase VEHICULO

        self.motor = kwargs['motor']
        self.n_puertas = kwargs['n_puertas']
        self.color = kwargs['color']
        self.fabricante = kwargs['fabricante']

    def changeFabricante(self, newFabricante):

        self.fabricante = newFabricante

if __name__ == '__main__':


    v1 = Vehiculo(motor=2.0, n_puertas= 4 ,color="blanco",fabricante="TOYOTA")

    f = open('file_obj.bin','wb')
    pickle.dump(v1,f)    # Serializamos el objeto v1 con el metodo 'dump'
    f.close()            # Cerramos la instancia f

    """ Deseralizando """

    def deserializar():

        f = open('file_obj.bin', 'rb' )
        vehicle = pickle.load(f)
        f.close()

        print(f'el carro es del fabricante Japones {vehicle.fabricante}')

    deserializar()

    v1.changeFabricante("Mitsubishi")
    print(f'el carro es del fabricante Japones {v1.fabricante}')
