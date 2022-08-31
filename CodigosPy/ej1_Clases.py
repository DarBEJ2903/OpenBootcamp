class Vehiculo:

    Color = 0
    Ruedas = 0
    Puertas = 0

    def color(self):
        self.Color = input("Ingrese el color del vehiculo: ")

    def numPuertas(self):
        self.Puertas = int(input("Ingrese el numero de puertas del Vehiculo: "))

    def numRuedas(self):
        self.Ruedas = int(input("Ingrese el numero de ruedas del vehiculo: "))

class Coche(Vehiculo):

    Velocidad = 0
    Cilindrada = 0

    def velocidad(self):
        self.Velocidad = float(input("Ingrese la velocidad del vehiculo (Km/h): "))

    def cilindrada(self):
        self.Cilindrada = float(input("Ingrese la cilindrada del motor: "))


miCoche = Coche()
miCoche.color()
miCoche.numPuertas()
miCoche.numRuedas()
miCoche.velocidad()
miCoche.cilindrada()
