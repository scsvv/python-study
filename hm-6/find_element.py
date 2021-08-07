import random


list1: list = [random.randrange(0, 100) for i in range(10)]
list2: list = [random.randrange(0, 100) for i in range(10)]

print(list1 + list2)

#Количество уникальных елементов 
print(len([0 for i in list1 + list2 if list1.count(i) == 1 and list2.count(i) < 1 or list1.count(i) < 1 and list2.count(i) == 1]))

#Для удобства (для проверки)
print([i for i in list1 + list2 if list1.count(i) == 1 and list2.count(i) < 1 or list1.count(i) < 1 and list2.count(i) == 1])
