import time

# time.localTime()
# retorna esto
# time.struct_time(tm_year=x, tm_mon=x, tm_mday=x, tm_hour=x, tm_min=x, tm_sec=x, tm_wday=x, tm_yday=x, tm_isdst=x)
# Accedo al tercer valor que es la hora local
hora = time.localtime()[3]

if (hora > 19):
    print("Es hora de ir a casa")
else:
    print("Faltan", 19 - hora, "horas para ir a casa")
