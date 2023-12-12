# to swap between p1 and p2 solutions is literally changing 10 lines, so it'll all be in this file

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

emptyRows = []
emptyColumns = []
galaxyPositions = []
total = 0

for i in range(len(lines)):
    found = False
    for j in range(len(lines[i])):
        if lines[i][j] != '.':
            found = True
            galaxyPositions.append([i, j])

    if not found:
        emptyRows.append(i)

for i in range(len(lines[0])):
    found = False
    for j in range(len(lines)):
        if lines[j][i] != '.':
            found = True

    if not found:
        emptyColumns.append(i)

"""print(emptyRows)
print(emptyColumns)
print(galaxyPositions)"""

for i in range(len(galaxyPositions) - 1):
    for j in range(i+1, len(galaxyPositions)):
        addValue = 0
        for r in emptyRows:
            if (galaxyPositions[i][0] < r < galaxyPositions[j][0]) or (galaxyPositions[i][0] > r > galaxyPositions[j][0]):
                # change to 1 for p1, 999999 for p2
                addValue += 999999
        for r in emptyColumns:
            if (galaxyPositions[i][1] < r < galaxyPositions[j][1]) or (galaxyPositions[i][1] > r > galaxyPositions[j][1]):
                # change to 1 for p1, 999999 for p2
                addValue += 999999
        t = abs(galaxyPositions[i][0] - galaxyPositions[j][0]) + abs(galaxyPositions[i][1] - galaxyPositions[j][1]) + addValue
        print(f"adding {t}")
        total += t

print(total)
