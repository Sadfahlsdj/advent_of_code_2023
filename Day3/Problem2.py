import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0
numbers = []

lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0])) # adds a line at beginning and end with just .


for i in range(len(lines)):
    for match in re.finditer('[0-9]+', lines[i]):
        numbers.append([match.start(), match.end(), i, match.group()])
        # generates array(s) with 4 elements - first index of number, last index, the row index, and its value
    lines[i] = '.' + lines[i] + '.'
    # adds a . at the start and end of each line

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
                    # print(f"added {a[3]} with index {a[2]}, {a[0]} from line {a[2]} based on character {lines[j][k]} at index {j}, {k}")
                    # total += a[3]
                    # print(f"added {a[3]} from line {a[2]}")
                    gearIndices.append([j, k, a[3]]) # index of row, index within row, and value respectively
                    return


for a in numbers:
    scanNumber(a)

# print(gearIndices)
for i in range(len(gearIndices)):
    for j in range(i+1, len(gearIndices)):
        if gearIndices[i][0] == gearIndices[j][0] and gearIndices[i][1] == gearIndices[j][1]:
            total += gearIndices[i][2] * gearIndices[j][2]
            # finds repeats, once one is found multiples the values and adds it
            # probably bad complexity


# print(numbers)
print(total)