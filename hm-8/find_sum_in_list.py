def find_sum_in_list(numbers_list, number = None):
    '''
    Функция принимает аргументы: список чисел и число. 
    Цель функции выяснить, есть ли в списке 2 числа сума которых еквивалентна числу переданому второму аргументу   
    '''


    list_length = len(numbers_list)

    if number == None: 
        print("Не правильное использование вызова функции")
        return False
    
    for i in range(0, list_length):
        for j in range(i+1, list_length):
            if( numbers_list[i] + numbers_list[j] == number):
                return True
    
    return False


num1 = find_sum_in_list([1,2,3,4,5,6,7,8,9], 10)
num2 = find_sum_in_list([1,2,3,4,5,6,7,8,9], 100)
print(num1, num2)

