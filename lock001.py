import threading
from time import sleep

control = threading.Lock()


def getarchivo1():
    control.acquire()
    print("getarchivo1(): Archivo 1")
    f = open("archivo1.txt", "w+")
    data = f.readline()
    print(data)
    sleep(4)  # simular que se esta trabajando con el archivo
    print("getarchivo1(): Archivo 1 finalizado")


def getarchivo2():
    control.acquire() -
    print("getarchivo2(): Archivo 2")
    f = open("archivo1.txt", "w+")
    data = f.readline()
    print(data)
    sleep(4)  # simular que se esta trabajando con el archivo
    print("getarchivo2(): Archivo 2 finalizado")
    control.release()


t1 = threading.Thread(target=getarchivo1)
t2 = threading.Thread(target=getarchivo2)

t2.start()
t1.start()
