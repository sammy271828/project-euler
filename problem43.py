import math
from useful_routines import isTriangle

def isPandigital(n):
    s = str(n)
    if n < 0:
        return isPandigital(-n)

    elif len(s) == 1:
        if n == 1:
            return True
        else:
            return False

    else:
        values = []

        for i in range(0, len(s)):
            values.append(s[i])

        values.sort()

        if values[0] != '0':
            return False
        else:
            counter = 0
            while counter < len(s) and values[counter]  == str(counter):
                counter += 1

            if counter == len(s):
                return True
            else:
                return False

arr = []

p = [2,3,5,7,11,13,17]

primes = [2,3,5,7,11,13,17,19,23,29]

table = []

for m in p:
    arr = []
    for i in range(10 // m, 1000 // m + 1):
        if m * i < 100:
            s = '0' + str(m * i)
        else:
            s = str(m * i)

        if len(s) == 3 and s[0] != s[1] != s[2] != s[0]:
            arr.append(s)

    print(len(arr))
    table.append(arr)

print(table[6])
print(table[5])
print(table[0])

values = []

for i1 in table[6]:
    for i2 in table[5]:

        if i1[0] + i1[1] == i2[1] + i2[2]:

            for i3 in table[4]:

                if i3[1] + i3[2] == i2[0] + i2[1]:

                    for i4 in table[3]:

                        if i4[1] + i4[2] == i3[0] + i3[1]:

                            for i5 in table[2]:

                                if i5[1] + i5[2] == i4[0] + i4[1]:

                                    for i6 in table[1]:

                                        if i6[1] + i6[2] == i5[0] + i5[1]:

                                            for i7 in table[0]:

                                                if i7[1] + i7[2] == i6[0] + i6[1]:

                                                    print(i7,i6,i5,i4,i3,i2,i1, i7[0] + i6[0] + i5[0] + i4[0] + i3[0] + i2[0] + i1)
                                                    values.append(i7[0] + i6[0] + i5[0] + i4[0] + i3[0] + i2[0] + i1)

print(values)

sum = 0

for i in range(1,10):
    s = str(i)
    for j in values:
        temp = int(s + j)
        if isPandigital(temp):
            sum += temp
            print(temp)

print(sum)