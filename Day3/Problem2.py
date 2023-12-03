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

gearIndices = []

def scanNumber(a):
    global total
    a[0], a[1], a[2], a[3] = int(a[0]), int(a[1]), int(a[2]), int(a[3])

    for i in range(a[0], a[1]):
        for j in range(a[2] - 1, a[2] + 2):
            for k in range(a[0], a[1] + 2):
                # print(j, k, a[2])
                if lines[j][k] == '*':
                    print(f"added {a[3]} with index {a[2]}, {a[0]} from line {a[2]} based on character {lines[j][k]} at index {j}, {k}")
                    # total += a[3]
                    # print(f"added {a[3]} from line {a[2]}")
                    gearIndices.append([j, k, a[3]])
                    return


for a in numbers:
    scanNumber(a)

# print(gearIndices)
for i in range(len(gearIndices)):
    for j in range(i+1, len(gearIndices)):
        if gearIndices[i][0] == gearIndices[j][0] and gearIndices[i][1] == gearIndices[j][1]:
            total += gearIndices[i][2] * gearIndices[j][2]


# print(numbers)
print(total)