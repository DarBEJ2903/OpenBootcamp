masa = input('Introduce tu masa en KG: ')
estatura = input('Introduce tu estatura (metros): ')
try:
    imc = float(masa)/(float(estatura)**2)
    print('Tu ìndice de masa corporal es: '+ str(round(imc,2)))
except ValueError:
    print ('Datos Ingresados Invalidos')
