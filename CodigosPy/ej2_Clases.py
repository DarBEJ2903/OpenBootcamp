class Alumnos:
    def __init__(self):
        Nombre = None
        Nota = None
        Nombre = Alumnos.ingresarNombre(self,Nombre)
        Nota = Alumnos.ingresarNota(self,Nota)
        if Nota>=3.0:
            print("Alumno Aprobo")
        else:
            print("Alumno Reprobo")


    def ingresarNombre(self,Nombre):

        Nombre = input("Ingresar nombre del alumno: ")
        return Nombre

    def ingresarNota(self,Nota):
        while True:
            try:
                Nota = float(input("Ingresar Nota del alumno (0-5.0): "))
                assert (Nota >= 0 and Nota<=5.0)
                return Nota
            except:
                print("INGRESE UN VALOR VALIDO")


alumno = Alumnos()
