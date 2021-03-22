import math
from useful_routines import primes, isPrime, numDigits, isPandigital

f = open('problem11.txt')
content = f.read()
print(len(content))

max_prod = 0

max = len(content)
print(content)

numbers = []

i = 0
while i < max:
    current_num = content[i] + content[i + 1]
    numbers.append(int(current_num))
    i += 3

print(numbers)
print(numbers[20])

grid = []

for i in range(0,20):
    row = []
    for j in range(0,20):
        row.append(numbers[j + 20 * i])
    grid.append(row)

print(grid)

max_prod = 0

for i in range(0,20):
    for j in range(0,20):
        if i >= 3:
            temp = grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j]
            if temp > max_prod:
                max_prod = temp
            if j >= 3:
                temp = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
                if temp > max_prod:
                    max_prod = temp
            if j <= 16:
                temp = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
                if temp > max_prod:
                    max_prod = temp

        if j >= 3:
            temp = grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3]
            if temp > max_prod:
                max_prod = temp


print(max_prod)