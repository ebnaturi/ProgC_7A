import threading
import time
import requests
import random

API_URL = "https://jsonplaceholder.typicode.com/posts/"

api_lock = threading.Lock()


def fetch_data(thread_name,id_val):
    time.sleep(random.randint(2,10))
    # Adquirimos el lock usando un context manager (with)
    with api_lock:
        print(f"[{thread_name}] Adquiriendo lock para obtener datos de la API...")

        # Simulamos la llamada a la API
        try:
            response = requests.get(API_URL+str(id_val))
            if response.status_code == 200:
                data = response.json()
                # Aquí podríamos procesar los datos
                print(f"[{thread_name}] Datos obtenidos con éxito: {data}")
            else:
                print(f"[{thread_name}] Error al obtener datos: {response.status_code}")
        except Exception as e:
            print(f"[{thread_name}] Excepción al llamar a la API: {e}")

    time.sleep(1)


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=fetch_data, args=(f"Hilo-{i}",(i+1),))
        threads.append(t)

    # Iniciamos todos los hilos
    for t in threads:
        t.start()

    # Esperamos a que todos los hilos terminen
    for t in threads:
        t.join()

    print("Todas las peticiones han finalizado.")


if __name__ == "__main__":
    main()
