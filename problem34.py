import math

factorials = [1]

for i in range(1,10):
    factorials.append(i * factorials[i-1])



def getDigits(n,arr = []):

    if n < 0:
        return "N/A"

    elif n == 0:
        arr.append(1)
        return arr

    elif n < 10:
        arr.append(n)
        return arr

    else:
        arr.append(n % 10)
        return getDigits(n // 10, arr)



max = 7 * factorials[9]
min = 3

total = 0

for i in range(min,max):
    sum = 0
    digits = getDigits(i,[])
    #print(digits)
    size = len(digits)

    for j in range(0,size):
        sum += factorials[digits[j]]

    if i == sum:
        print(i)
        total += i


print(total)