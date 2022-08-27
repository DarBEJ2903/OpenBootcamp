edad = input('Ingrese su Edad: ')
try:
    if int(edad) >= 18:
        print("Es Mayor de Edad")
    else:
        print("No es mayor de edad")
except ValueError:
    print("Dato ingresado erroneo")