from random import randint

my_list: list = [i for i in randint(10)]
k = randint(0, 9)

print(f'k = {k}, елемент с этим номером = {my_list[k]}')

for i in range(k, len(my_list)-1):
    my_list[i] = my_list[i+1]

my_list.pop()
print(my_list)
