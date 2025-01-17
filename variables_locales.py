import threading
import time
import random

# datos_locales = threading.local()
# random.uniform(0, 3)
valor = "X"


def funcion_principal(val):
    # Asignamos algo a 'datos_locales'
    # datos_locales.valor = valor
    global valor
    valor = val
    time.sleep(1)
    print(f"{threading.current_thread().name} => datos_locales.valor = {valor}")


# Creamos dos hilos que usan la misma función, pero con valores distintos.
hilo1 = threading.Thread(target=funcion_principal, args=("A",), name="Hilo-1")
hilo2 = threading.Thread(target=funcion_principal, args=("B",), name="Hilo-2")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
print("el valor de la variable local es: ", valor)
