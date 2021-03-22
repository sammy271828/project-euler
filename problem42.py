import math
from useful_routines import isTriangle

f = open('words42.txt')
content = f.read()
print(content)

names = []

s = ''

for i in range(0,len(content)):
    if content[i] == ',':
        names.append(s)
        s = ''
    elif content[i] != '"':
        s += content[i]
names.append(s)

print(names[0])
scores = 0
counter = 0

for i in range(0, len(names)):
    score = 0
    current_name = names[i]
    for j in range(0,len(current_name)):
        score += ord(current_name[j]) - 64

    if isTriangle(score):
        counter += 1

print(counter)


