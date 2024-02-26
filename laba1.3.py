import math
import random
import time


n = input('введите количество строк: ')
m = input('введите колиество столбцов: ')

min_limit = input('введите минимально значение: ')
max_limit = input('введите максимальное значени: ')

try:
    mtrx = [[random.randrange(int(min_limit), int(max_limit)) for j in range(int(m))] for i in range(int(n))]
except:
    print('min_value and max_value are the same')
    exit()


# сортировка выбором
mtrx_select = [mtrx[i].copy() for i in range(int(n))]

start_time = time.time()

for k in range(int(n)):
    for i in range(0, int(m) - 1):
        smallest = i
        for j in range(i + 1, int(m)):
            if mtrx_select[k][j] < mtrx_select[k][smallest]:
                smallest = j
        mtrx_select[k][i], mtrx_select[k][smallest] = mtrx_select[k][smallest], mtrx_select[k][i]


print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))

########################

# сортировка вставками
mtrx_insert = [mtrx[i].copy() for i in range(int(n))]
start_time = time.time()
for k in range(int(n)):
    for i in range(1, int(m)):
        temp = mtrx_insert[k][i]
        j = i - 1
        while (j >= 0 and temp < mtrx_insert[k][j]):
            mtrx_insert[k][j + 1] = mtrx_insert[k][j]
            j = j - 1
        mtrx_insert[k][j + 1] = temp
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
######################

# сортировка пузырьком
mtrx_bubble = [mtrx[i].copy() for i in range(int(n))]
start_time = time.time()

for k in range(int(n)):
    for i in range(int(m) - 1):
        for j in range(int(m) - i - 1):
            if mtrx_bubble[k][j] > mtrx_bubble[k][j + 1]:
                mtrx_bubble[k][j], mtrx_bubble[k][j + 1] = mtrx_bubble[k][j + 1], mtrx_bubble[k][j]
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
######################

# сортировка Шелла
mtrx_shell = [mtrx[i].copy() for i in range(int(n))]
start_time = time.time()

for h in range(int(n)):
    n = len(mtrx_shell[h])
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = mtrx_shell[h][i]
            j = i
            while j >= interval and mtrx_shell[h][j - interval] > temp:
                mtrx_shell[h][j] = mtrx_shell[h][j - interval]
                j -= interval
            mtrx_shell[h][j] = temp
        k -= 1
        interval = 2 ** k - 1

print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
######################


# быстрая сортировка
mtrx_quick = [mtrx[i].copy() for i in range(int(n))]
start_time = time.time()

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

for i in range(int(n)):
    mtrx_quick[i] = quicksort(mtrx_quick[i])

print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
######################


# быстрая турнирная
mtrx_tur = [mtrx[i].copy() for i in range(int(n))]
start_time = time.time()

def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1

def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)

for i in range(int(n)):
    heapsort(mtrx_tur[i])

print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
######################

