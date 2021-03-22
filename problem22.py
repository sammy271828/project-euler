import math

f = open('names22.txt')
content = f.read()
print(content)

names = []
names.append('A')
s = ''

for i in range(0,len(content)):
    if content[i] == ',':
        names.append(s)
        s = ''
    elif content[i] != '"':
        s += content[i]
names.append(s)

print(names)

names.sort()
print(names)

sum = 0

for i in range(1, len(names)):
    score = 0
    current_name = names[i]
    for j in range(0,len(current_name)):
        score += ord(current_name[j]) - 64
    score *= i

    sum += score

print(sum)