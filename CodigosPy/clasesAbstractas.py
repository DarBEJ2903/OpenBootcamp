from abc import ABC, abstractmethod

#Declarando la clase ABSTRACTA
class Persona(ABC):
    @abstractmethod
    def Nombre(self):
        pass

    def genero(self):
        print("Masculino")

#Las clases abstractas no pueden ser instanciadas,se tiene que heredar de ellas
#La clase Alumno hereda de la clase abstracta Persona
class Alumno(Persona):
    def Nombre(self):
        print("Mi nombre es Daniel")


primeraPersona = Alumno()
primeraPersona.Nombre()

