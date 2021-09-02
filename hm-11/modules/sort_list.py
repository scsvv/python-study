from random import randint

sum : list = list()

def sort_matrix(list_matrix: list):

    for column in list_matrix:
        M = len(sum)
        sum.append(0)
        for item in column:
            sum[M] += item

    for i in range(len(sum) - 1):
        for j in range(len(sum) - 2, i - 1, -1):
            
            if sum[j + 1] < sum[j]:
                sum[j], sum[j + 1] =  sum[j + 1], sum[j]
                for row in range(0, len(sum)):
                    list_matrix[row][j], list_matrix[row][j + 1] =  list_matrix[row][j + 1], list_matrix[row][j]  
    
    for i in range(len(sum)):
        for j in range(len(sum) - 1):
            for k in range(len(sum) - 2, -1, -1):
                
                if i % 2 == 0:
                    
                    if list_matrix[k][i] < list_matrix[k + 1][i]:
                        list_matrix[k][i], list_matrix[k + 1][i] = list_matrix[k + 1][i], list_matrix[k][i]
                else: 
                    if list_matrix[k + 1][i] < list_matrix[k][i]:
                        list_matrix[k][i], list_matrix[k + 1][i] = list_matrix[k + 1][i], list_matrix[k][i]



def print_list(list_matrix : list) -> None:
    list_matrix.append(sum)
    for i in range(len(list_matrix)):
        for j in range(len(list_matrix)-1):
            print(f"{list_matrix[i][j] : > 4}", end='')
        print()
    list_matrix.pop()
