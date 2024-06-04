from queue import Queue
import random
import time

# Створити чергу заявок
queue = Queue()


# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги
def generate_request():
    request = random.randint(1, 999)
    queue.put(request)
    print(f"Заявка {request} створена")


# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Заявка {request} оброблена")
    else:
        print("Черга пуста")


# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок
def main():
    while True:
        command = input(
            "Введіть команду: g-створити заявку, p-обробити заявку, e-вийти з програми: "
        )
        if command == "e":
            break
        elif command == "g":
            generate_request()
            time.sleep(1)
        elif command == "p":
            process_request()
            time.sleep(1)


if __name__ == "__main__":
    main()
