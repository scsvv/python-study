from random import randint 

machine_mumber = randint(1, 100)
count = 0

while True:
    user_mumber = input("Отгадайте число от 1 до 100: ")
    count += 1
    try: 
        user_mumber = int(user_mumber)
    except ValueError:
        user_mumber = -100
    
    if user_mumber == machine_mumber:
        print(f'Вы угадали моё число\nКоличество попыток: {count}')
        break
    elif user_mumber == -100:
        print(f'Введите число!!!!!')
    elif user_mumber > machine_mumber: 
        print(f'Моё число меньше')
    elif user_mumber < machine_mumber: 
        print(f'Моё число больше')
    





