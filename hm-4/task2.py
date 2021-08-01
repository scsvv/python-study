N = int(input('Введите число: '))

mod = 10
for i in range(1, N + 1):
    if i == mod:
        mod *= 10
    if (i * i) % mod == i:
        print(f'{i}*{i} = {i**2}')