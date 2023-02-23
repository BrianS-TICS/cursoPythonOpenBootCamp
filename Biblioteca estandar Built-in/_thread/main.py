# Programacion miltihilo
import _thread
import time

def horaActual(nombre_thread, tiempo_espera) :
    time.sleep(tiempo_espera)
    print(f"Nombre : {nombre_thread} | {time.ctime(time.time())}")

_thread.start_new_thread(horaActual, ("thread 1", 2))
_thread.start_new_thread(horaActual, ("thread 2", 5))

print("Se han disaparado los hilos")

time.sleep(10)