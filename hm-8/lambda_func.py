from random import randint

numbers_list = [randint(1, 10) for i in range(1, 5)]
power = randint(2, 5)

power_lambda = lambda x, y=1: x**y

powered_numbers = None

power = int(power)
powered_numbers = map(power_lambda, numbers_list, [power]*len(numbers_list))

print(f'list = {list(numbers_list)}, power = {power}')
print(list(powered_numbers))