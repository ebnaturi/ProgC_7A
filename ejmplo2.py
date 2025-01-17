from threading import Thread, current_thread, Timer, active_count, excepthook
from time import sleep
import random
import threading

# myvars =threading.local()
myvars = 0


class MyHilo(Thread):
    valor = 0

    def __init__(self, tiempo):
        Thread.__init__(self)
        self.valor = tiempo

    def run(self):
        global myvars
        myvars = self.valor
        print("soy el hilo con el tiempo,", myvars)
        # try:
        if self.valor > 3:
            raise Exception("Tiempo de espera agotado.....................")
        sleep(self.valor)
        # except Exception as e:
        #    print(e)
        print("He acabado")


def hook_Except(args):
    print("Excepcion en el hilo: ")


threading.excepthook = hook_Except
hilos = []
for i in range(20):
    t1 = MyHilo(random.uniform(0, 5))
    hilos.append(t1)

for hx in hilos:
    hx.start()

for hx in hilos:
    hx.join()

print(active_count())
