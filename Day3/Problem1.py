import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0
numbers = []

lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))

# each line is 140 characters long
for i in range(len(lines)):
    for match in re.finditer('[0-9]+', lines[i]):
        numbers.append([match.start(), match.end(), i, match.group()])
    lines[i] = '.' + lines[i] + '.'

# print(numbers)
# print(len(lines[17]))



def scanNumber(a):
    global total
    numberAdded = False
    a[0], a[1], a[2], a[3] = int(a[0]), int(a[1]), int(a[2]), int(a[3])

    for i in range(a[0], a[1]):
        for j in range(a[2] - 1, a[2] + 2):
            for k in range(a[0], a[1] + 2):
                # print(j, k, a[2])
                if not lines[j][k].isnumeric() and not lines[j][k] == '.':
                    print(f"added {a[3]} with index {a[2]}, {a[0]} from line {a[2]} based on character {lines[j][k]} at index {j}, {k}")
                    if not numberAdded:
                        total += a[3]
                        # print(f"added {a[3]} from line {a[2]}")
                        numberAdded = True
                        return



for a in numbers:
    scanNumber(a)

# print(numbers)
print(total)