import math

a = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
b = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

day_of_week = 2

sundays = 0

year = 1901

while year < 2001:
    for i in range(0, 12):
        if day_of_week % 7 == 0:
            sundays += 1
        if year % 4 == 0:
            day_of_week += b[i]
        else:
            day_of_week += a[i]
    year += 1


x = 3*(333*334/2) + 5*199*200/2

sum = 0

i = 3

bound = 1000

while i < bound:
    sum+=i
    i+=3

j = 5

while j<bound:
    sum+=j
    j+=5

k = 15

while k<bound:
    sum -= k
    k += 15

print(sum)

