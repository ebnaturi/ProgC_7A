import threading
import time

# Crear un bloqueo reentrante
rlock = threading.Lock()

def funcion_a():

    with rlock:
        print(f"{threading.current_thread().name} - funcion_a: Inicio de sección crítica")
        time.sleep(0.5)

        print(f"{threading.current_thread().name} - funcion_a: Llamando a funcion_b()")
        funcion_b()

        print(f"{threading.current_thread().name} - funcion_a: Fin de sección crítica")

def funcion_b():

    with rlock:
        print(f"{threading.current_thread().name} - funcion_b: Inicio de sección crítica")
        time.sleep(0.5)
        print(f"{threading.current_thread().name} - funcion_b: Fin de sección crítica")

def main():
    hilo1 = threading.Thread(target=funcion_a, name="Hilo-1")
    hilo2 = threading.Thread(target=funcion_a, name="Hilo-2")

    hilo1.start()
    hilo2.start()

    # Esperar a que ambos hilos terminen
    hilo1.join()
    hilo2.join()

if __name__ == "__main__":
    main()
