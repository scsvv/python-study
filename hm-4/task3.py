NUMBER = input("Введите натуральное число: ")
LENGTH = len(NUMBER)

print(NUMBER, LENGTH)

for i in range(1, (LENGTH-1) , 1):
    if NUMBER[i] == NUMBER[i - 1] or NUMBER[i] == NUMBER[i + 1]:
        print("Да")
        break
else:
    print("Нет")