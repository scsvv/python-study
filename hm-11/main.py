from random import randint

from own_lib import * 
from modules.sort_list import *

if __name__ == "__main__":

    print(reverse_it(1234))
    print(count_first(None, 12))

    matrix: list = [[randint(1, 50) for j in range(10)] for i in range(10)]
    sort_matrix(matrix)
    print_matrix_with_sums(matrix)
