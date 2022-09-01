from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    if((now.hour>19) and (now.minute>0)):
        print("ES HORA DE IR A CASA")
    else:
        if now.minute>0:
            minW = 60 - now.minute
            hourW = 19 - (now.hour + 1)
        else:
            hourW = 19  - now.hour
        print("FALTAN: ",hourW," Horas y ",minW," Minutos De Trabajo")