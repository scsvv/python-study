from typing import List


from random import randint

my_list: list = [i for i in range(10)]
k = randint(0, 9)
C = randint(1, 9) * 11

print(f'на позицию под номером {k} (0 - 9) поставить эллемент {C}')

my_list.append(my_list[len(my_list) - 1])
for i in range(len(my_list) -1, k - 1, -1):
    my_list[i] = my_list[i - 1]
my_list[i] = C

print(my_list)

