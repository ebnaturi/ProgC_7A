import threading
import time
import random

buffer = []
capacidad_buffer = 5

condition = threading.Condition()


def productor():

    for _ in range(10):
        item = random.randint(1, 100)
        with condition:
            while len(buffer) >= capacidad_buffer:
                condition.wait()
            buffer.append(item)
            print(f"[Productor] Produjo {item}")
            condition.notify_all()
        time.sleep(random.random())


def consumidor(nombre):
    for _ in range(5):
        with condition:

            while not buffer:
                condition.wait()

            item = buffer.pop(0)
            print(f"[Consumidor {nombre}] Consumió {item}")

            condition.notify_all()

        time.sleep(random.random())


def main():
    # Creamos los hilos: 1 productor y 2 consumidores
    h_productor = threading.Thread(target=productor)
    h_consumidor1 = threading.Thread(target=consumidor, args=("A",))
    h_consumidor2 = threading.Thread(target=consumidor, args=("B",))

    # Iniciamos los hilos
    h_productor.start()
    h_consumidor1.start()
    h_consumidor2.start()

    # Esperamos a que finalicen todos
    h_productor.join()
    h_consumidor1.join()
    h_consumidor2.join()

    print("Proceso completado.")


if __name__ == "__main__":

    main()
