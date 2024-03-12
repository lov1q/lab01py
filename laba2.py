import random

def generate_random_list(num_elements):
    journal_number = 7
    min_range = 5
    max_range = journal_number * 100
    random_list = [random.randint(min_range, max_range) for _ in range(num_elements)]
    return random_list

# Пример вызова функции с указанным числом элементов
num_elements = 17
random_list = generate_random_list(num_elements)
print(random_list)
