from threading import Thread, current_thread, Timer
from time import sleep


def hilo1(tiempo):
    print("iniiciando HIloooooooooooo", current_thread().ident)
    sleep(tiempo)  # el programa hace algo y tarda 3 ms para hacerlo
    print("Ya acabe.....................", current_thread().name)


def hilo2(tiempo=1):
    print("iniiciando HIloooooooooooo", current_thread().ident)
    sleep(tiempo)  # el programa hace algo y tarda 3 ms para hacerlo
    print("Ya acabe.....................", current_thread().name)


def hilotiempo():
    print("iniiciando HIloooooooooooo", current_thread().name)
    sleep(2)  # el programa hace algo y tarda 3 ms para hacerlo
    print("Ya acabe.....................", current_thread().name)


h1 = Thread(target=hilo1, args=(1,), name="elias")
h2 = Thread(target=hilo2, args=(4,), daemon=True, name="Batalla")
ht3 = Timer(1, hilotiempo)
h1.start()
h2.start()
ht3.start()
sleep(3)
if (h2.is_alive()):
    print(" esta vivo")
ht3.cancel()
h1.join()
print("Se ha terminado el programa")
