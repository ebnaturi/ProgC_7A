import threading
import time
import random

shared_value = None


lock = threading.Lock()
condition = threading.Condition(lock)


def producer():
    global shared_value
    for _ in range(5):
        with condition:
            val = random.randint(1, 100)
            shared_value = val
            print(f"[Producer] produjo: {val}")

            condition.notify()

        time.sleep(0.5)


def consumer():
    global shared_value
    for _ in range(5):
        with condition:
            while shared_value is None:
                condition.wait()

            print(f"[Consumer] consumió: {shared_value}")
            shared_value = None

        time.sleep(0.5)


def main():
    t_producer = threading.Thread(target=producer)
    t_consumer = threading.Thread(target=consumer)


    t_producer.start()
    t_consumer.start()


    t_producer.join()
    t_consumer.join()

    print("Ejecución completada.")


if __name__ == "__main__":
    main()
