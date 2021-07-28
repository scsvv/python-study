from random import randint

#Два числа выбираются случайно для удобства
a = randint(-100, 100)
b = randint(-100, 100)
print(f'a = {a}, b = {b}')

#Смысл магии изменеия в том, что мы находим разницу между числами и с её полмощью мы с помощью арифметики нходим 
if a == b: print(f'a = {a}, b = {b}')
elif a > b: # a = 10 | b = 3
    a -= b  # a = (10 - 3) = 7 | b = 3
    b += a  # b = (a + b) = (7 + 3) = 10 | b = 10
    a = b - a # a = 10 - 7 = 3 | a  = 3
    print(f'a = {a}, b = {b}')
elif b > a:
    b -= a
    a += b
    b = a - b
    print(f'a = {a}, b = {b}')
else: 
    print("Invalid")

'''
Также как вариант 

a ^= b
b ^= a
a ^= b

'''