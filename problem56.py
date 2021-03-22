import math

total = 0


def format(number):
    carry = 0

    for i in range(0,len(number)):
        temp = number[i] // 10
        val = number[i] % 10 + carry
        carry = temp

        if val < 10:
            number[i] = val
        else:
            number[i] = val % 10
            carry += val // 10


    if 0 < carry < 10:
        number.append(carry)
    elif carry >= 10:
        number.append(carry % 10)
        number.append(carry // 10)

    return number


arr = [99,99,99]

print(format(arr))


for a in range(99,100):
    number = [1]
    for b in range(1,100):
        for i in range(0,len(number)):
            number[i] *= a

        number = format(number)
        #number.reverse()
        print(number)
        print(a ** b)

        if sum(number) > total:
            total = sum(number)


print(total)