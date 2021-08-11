from random import randint

list1: list = [randint(0, 100) for i in range(10)]
list2: list = [randint(0, 100) for i in range(10)]

# Вывод занчений внури списков для проверки 
print(list1, "|" ,list2)

# выполнение задания 
print(len(set(list1) & set(list2)))

# для удобства проверки 
print(f'Numbers: {(set(list1) & set(list2))}')
