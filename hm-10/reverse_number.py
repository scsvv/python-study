from math import log10
import math

def reverse_it(n: int) -> int:

    '''
    remainder - хранит в себе послднюю цифру внутри числа
    integer - хрнит все цифры числа, кроме последнего 
    quantity_of_decade - хранит в себе количество 10 разрядов в числе
    '''

    if n > 10:
        remainder  = n % 10
        integer = n // 10
        quantity_of_decade = int(log10(integer) + 1)

        return remainder * 10 ** quantity_of_decade + reverse_it(integer)

    else:
        return n

if __name__ == "__main__":
    print(reverse_it(179))
    