from random import randint

numbers_list: list = [randint(0, 100) for i in range(10)]

# Список чисел
print(numbers_list)

# Количество еементов
print(f'Количество различных чисел: {len(set(numbers_list))}')