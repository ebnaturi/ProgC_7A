import threading
import time


def tarea(num):
    contador = 0  # Variable local
    for _ in range(num):
        contador += 1
    print(f"El hilo {threading.current_thread().name} terminó con contador={contador}")


hilo1 = threading.Thread(target=tarea, args=(5,), name="Hilo-1")
hilo2 = threading.Thread(target=tarea, args=(10,), name="Hilo-2")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
