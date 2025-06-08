import threading
import time
import random

# Завдання 1: Зворотний відлік
def countdown():
    for i in range(10, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(1)

# Завдання 2: Симуляція завантаження
def download_file(file_id):
    duration = random.randint(3, 5)
    time.sleep(duration)
    print(f"File {file_id} downloaded in {duration} seconds")

# Завдання 3: Паралельна обробка даних
def calculate_sum(data_slice, result_list, index):
    result_list[index] = sum(data_slice)

def main():
    print("\n--- Завдання 1: Зворотний відлік ---")
    t1 = threading.Thread(target=countdown)
    t1.start()
    t1.join()  # Дочекаємося завершення зворотного відліку перед наступним завданням

    print("\n--- Завдання 2: Симуляція завантаження ---")
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=download_file, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n--- Завдання 3: Паралельна обробка даних ---")
    numbers = [random.randint(1, 100) for _ in range(1000)]
    parts = [numbers[i::4] for i in range(4)]  # Розбиття на 4 частини
    results = [0] * 4
    threads = []

    for i in range(4):
        t = threading.Thread(target=calculate_sum, args=(parts[i], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = sum(results)
    print(f"Total sum: {total}")

if __name__ == "__main__":
    main()
