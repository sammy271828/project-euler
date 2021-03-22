import math

array = [[0,1]]

max = 28123

for i in range(1, max+1):
    array.insert(i,[i,1])


for i in range(2, max // 2):
    m = 2*i
    while m <= max:
        array[m][1] += i
        m += i

total = 0

abundant = []

for i in range(1, max+1):
    if i < array[i][1]:
        abundant.append(i)

length = len(abundant)

abundant_sums = []

for i in range(0, length):
    for j in range(0,length):
        abundant_sums.append(abundant[i] + abundant[j])

length2 = len(abundant_sums)

lowest = 2*abundant[0]

#for i in range(1, max+1):
#
#    val = True
#
#    if i < lowest:
#        total += i
#
#    else:
#        current_index = 0
#
#        while i >= abundant[current_index]:
#
#            for j in range(0,current_index+1):
#
#                if abundant[j] + abundant[current_index] > i:
#                    break
#
#                elif abundant[j] + abundant[current_index] == i:
#                    val = False
#
#            current_index += 1

 #           if current_index >= length:
 #                 break

#    if val:
#        total += i

total = 0

#for i in range(1, max + 1):
#    val = True
#    if i < abundant_sums[0]:
#        continue
#    else:
#        for j in range(0, length2):
#            if i == abundant_sums[j]:
#                val = False
#                break
#    if val:
#        total += i


print(total)
abundant_sums.sort()

current_index = 0
n = max * (max+1) // 2

while abundant_sums[current_index] <= max:
    if current_index > 0 and abundant_sums[current_index] == abundant_sums[current_index - 1]:
        current_index += 1
    else:
        n -= abundant_sums[current_index]
       #print(abundant_sums[current_index])
        current_index += 1



#print(abundant_sums)


print(n)