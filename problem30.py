import math

def powers(N):
    if N == 0:
        return 0

    M = N % 10
    return M**5 + powers(N // 10)

answers = []

for i in range(10,200000):
    if i == powers(i):
        answers.append(i)


total = 0

for i in range(0,len(answers)):
    total += answers[i]

print(total)

