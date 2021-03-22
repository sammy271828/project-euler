import math

array = [[0,1]]

max = 10000

for i in range(1, max+1):
    array.insert(i,[i,1])


for i in range(2, max // 2):
    m = 2*i
    while m <= max:
        array[m][1] += i
        m += i

total = 0

for i in range(1, max+1):
    n = array[i][1]
    if n <= max and array[n][1] == i and n != i:
        total += i
        print(i)
        print(n)
        print(' ')



print(total)