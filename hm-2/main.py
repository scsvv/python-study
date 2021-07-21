ProgramName = '**** ***   *** *****\n*    *  * *  *   *\n*    ***   ***   *\n*    *  *  * *   *\n**** ***  *  *   *\n'
print("task 5: \n\n" + ProgramName)

'''
output of line 2:  

**** ***   *** *****
*    *  * *  *   *
*    ***   ***   *
*    *  *  * *   *
**** ***  *  *   *
'''

print(
    '''
    task 6: 
    \\a - Bell(allert)
    \\b - Backspace
    \\n - New line
    \\t - Horizontal tab
    \\\ - Backslash \\
    \\" - Double quotation mark "
    \\' - Single quotation mark '
    '''
)



print("task 7")
name = input("Привет меня зовут Жарвис а тебя как зовут : ")
input(f'Как дела {name}?: ') #не создаю переменную под это выражение, так как информация, не используется и не стоит засорять память этой инфой (моё мнение)

x = input("Загадай число первое число: ")
y = input("Загадай число второе число: ")

try: 
    z = int(x) + int(y)
except ValueError: 
    z = 0

print(f'Сумма чисел равна {z}')

