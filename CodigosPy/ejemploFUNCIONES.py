#Se declara una funciòn con parametros opcionales
def paramOpcional(param1 = "Enero",param2 = "Agosto"):
    print(param1,param2)

paramOpcional() #Se llama a a la funcion sin parametros
paramOpcional("Abril","Mayo") #Se llama a la funcion pasandole dos parametros
#------------------------------------------------------------------------------#

#Se declara una funcion con parametros dinamicos
def paramDinamicos(*args):
    print(args)
paramDinamicos("Hola","Edad",25,6.3) #Se llama a la funcion con 'n' numero de parametros pueden ser màs o menos parametros.
#-----------------------------------------------------------------------------------------------#

#Se declara la funcion que recibe parametros con nombre:
def paramName(**kwargs):
    ## Verifica que exista en el diccionario kwargs la variable nombre
    if 'Nombre' in kwargs and kwargs['Nombre'] == 'Andres':
        print(kwargs)
paramName(Nombre = "Daniel", Edad = 25 , Telefono = 321427 , Ciudad = "Bogtà")
#---------------------------------------------------------------------------------#

#Operador ternario: Sirve para evitar errores de ejecución cuándo se llama a una función si un parametro esperado.

def opTernario (**kwargs):

    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0 # Aplicando el operador ternario 'if ...'
    final = kwargs ['final'] if 'final' in kwargs else inicial #Aplicando el operador ternario 'if ...'
    resultado = 0;
    for i in range (inicial,final + 1):
        resultado += i
    return  resultado

print(opTernario(inicial=12, final=15))
# ------------------------------------------------------------------------------------------------------------#

# FUNCION ANONIMA:  ES UNA FUNCION ESPECIAL QUE SE LE ASIGNA A UNA VARIABLE, EN PYTHON
# SE DECLARAN CON LA PALABRA RESERVADA LAMBDA:

funcionAnonima = lambda parametro1,parmetro2: parametro1 + parmetro2; #Declarando la funcion anonima
print(funcionAnonima(2,3)) # Llamando la funcion anonima pasando como parametros los numeros 2,3

# --------------------------------------------------------------------------------------------------#