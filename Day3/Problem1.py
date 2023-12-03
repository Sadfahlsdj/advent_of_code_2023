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

def scanNumber(a):
    global total
    a[0], a[1], a[2], a[3] = int(a[0]), int(a[1]), int(a[2]), int(a[3]) # just in case

    for i in range(a[0], a[1]): # loops over indices in the number
        for j in range(a[2] - 1, a[2] + 2): # loops over previous row thru next row
            for k in range(a[0], a[1] + 2): # loops over character before start to character after end
                # print(j, k, a[2])
                if not lines[j][k].isnumeric() and not lines[j][k] == '.':
                    print(f"added {a[3]} with index {a[2]}, {a[0]} from line {a[2]} based on character {lines[j][k]} at index {j}, {k}")
                    total += a[3]
                    return # this return statement makes it so numbers aren't double counted



for a in numbers:
    scanNumber(a)

# print(numbers)
print(total)