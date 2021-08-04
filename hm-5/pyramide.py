columns = input("Введите число от 3 до 9: ")

try: 
    columns = int(columns)
except ValueError:
    columns = 0

if columns >= 3 and columns <= 9:
    for i in range(1, columns + 1):
        #
        row = ''

        #подсчёт количества елементов внутри ряда. (1, 3, 5, 7, 9, 11, 13)
        COUNT = (i * 2) - 1
        
        #стартовое значение 1 элемента строки 
        symbol = 1

        #растут ли значения в ряду или нет? 
        is_up = True

        for j in range(1, COUNT + 1):
            row += str(symbol)
            if(is_up and symbol < i):
                symbol += 1
            elif(i == symbol):
                is_up = False
                symbol -= 1
            else: 
                symbol -= 1

        print(row)
else:
     print(f"В ввели не действительное значение")

