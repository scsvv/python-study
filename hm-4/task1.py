NUMBER = input("Введите натуральное число: ")

for i in NUMBER: 
    if NUMBER.count(i) > 1:
        print("Да")
        break
else:
    print("Нет")