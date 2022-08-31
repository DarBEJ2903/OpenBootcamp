#COMPOSICION DE CLASE: Se trata de instaciar clases dentro de otra clase
class Motor:
    motor = "V8 Diesel"

class Puertas:
    numero_Puertas = 0
    def sumPuertas(self):
        self.numero_Puertas = self.numero_Puertas + 1

class Carroceria:
    puertas = Puertas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

miCoche = Coche()
miCoche.carroceria.puertas.sumPuertas()
print(miCoche.motor.motor)
print(miCoche.carroceria.puertas.numero_Puertas)