import random
import time


n = input('введите количество строк: ')
m = input('введите колиество столбцов: ')

min_limit = input('введите минимально значение: ')
max_limit = input('введите максимальное значени: ')

try:
    mtrx = [[random.randrange(int(min_limit), int(max_limit)) for j in range(int(m))] for i in range(int(n))]
except:
    print('мин и макс равны')
    exit()

for i in range(int(n)):
    for j in range(int(m)):
        print(mtrx[i][j], end=' ')
    print()


