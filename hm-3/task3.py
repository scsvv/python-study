# Пользователь вводит предполагаемую дату
YEAR = input("Введите год от 1900 до 1000000: ")

# Проверка является ли дата числом?
try: 
    YEAR = int(YEAR)
except ValueError:
    YEAR = 0

# Проверка соответствия условий для числа
if YEAR < 1900 or YEAR > 1000000: print("invalid value")
else: 
    # Проверка на высокостность от большого делителя к меньшему
    if YEAR % 400 == 0: print(f'{YEAR} is leep year')
    elif YEAR % 100 == 0: print(f'{YEAR} is not leep year')
    elif YEAR % 4 == 0: print(f'{YEAR} is leep year')
    else: print(f'{YEAR} is not leep year')