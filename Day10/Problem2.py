import numpy as np
from Floodfill import * # floodfill algo in separate file to save space
np.set_printoptions(suppress=True)

currentInput = 'input.txt' # for hardcoding what pipe S is

with open(currentInput) as f:
    lines = [line.rstrip() for line in f]

def Insert (source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
"""


# my S is a | tile for the actual input
for i in range(len(lines)):
    # padding input with . to avoid oob errors
    lines[i] = Insert(lines[i], '.', 0)
    lines[i] = Insert(lines[i], '.', len(lines[i]))

lines.insert(0, '.' * len(lines[0])) # padding up/down
lines.append('.' * len(lines[0]))
# print(lines[0])

floodfillMap = arr = [[0 for i in range(len(lines[0]) * 3)] for j in range(len(lines) * 3)] # will be used for getting area

counter = 0 # back to 0 for floodfill algo
startPos = [-1, -1]
startSPos = [-1, -1] # position to check if the loop is done

direction = 0 # direction that the last connection came from, opposite of the direction that I just went
# 0 = up, 1 = right, 2 = down, 3 = left
# first connection goes down from start point, so initialized to 0

for l in lines:
    for i in l:
        if i == 'S':
            startPos = [lines.index(l) + 1, l.index(i)]
            startSPos = [lines.index(l), l.index(i)]
            # little bit of hardcoding, I will start at the | tile underneath the S
    # print(l)

currentPos = [startPos[0], startPos[1]]
current = lines[currentPos[0]][currentPos[1]]

# hardcoding what S starts as, as well as what bits in the bitmap it represents
if currentInput == 'example1.txt' or currentInput == 'example2.txt' or currentInput == 'example3.txt':

    lines[startSPos[0]] = lines[startSPos[0]].replace('S', 'F')
    floodfillMap[startSPos[0] * 3 + 1][startSPos[1] * 3 + 1] = 1
    floodfillMap[startSPos[0] * 3 + 1][startSPos[1] * 3 + 1 + 1] = 1
    floodfillMap[startSPos[0] * 3 + 1 + 1][startSPos[1] * 3 + 1] = 1
elif currentInput == 'input.txt':
    lines[startSPos[0]] = lines[startSPos[0]].replace('S', '|')
    floodfillMap[startSPos[0] * 3 + 1][startSPos[1] * 3 + 1] = 1
    floodfillMap[startSPos[0] * 3 + 1 - 1][startSPos[1] * 3 + 1] = 1
    floodfillMap[startSPos[0] * 3 + 1 + 1][startSPos[1] * 3 + 1] = 1

# generating the main loop, as well as what tiles on the bitmap are part of the main loop
# each tile represents a 3x3 area
"""
for example: a L tile becomes
0 1 0
0 1 1
0 0 0
"""
while currentPos != startSPos: # end condition
    floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1] = 1
    current = lines[currentPos[0]][currentPos[1]]
    up, right = lines[currentPos[0] - 1][currentPos[1]], lines[currentPos[0]][currentPos[1] + 1]
    down, left = lines[currentPos[0] + 1][currentPos[1]], lines[currentPos[0]][currentPos[1] - 1]
    # manually check up, left, right, down, left for each one

    movedTo = "" # diagnostic purposes

    # current = |, 7, or F and adjacent = |, L, or J: down connection
    # current = |, L, or J and adjacent = |, 7, or F: up connection
    # current = F, L, or - and adjacent = J, 7, or -: right connection
    # current = J, 7, or - and adjacent = F, L, or -: left connection
    # print(f"current is {current}, up, right, down, and left respectively are {up}, {right}, {down}, {left}")
    # next conditionals are checking which pipe to move to
    if (current == '|' or current == 'L' or current == 'J') and (up == '|' or up == '7' or up == 'F') and direction != 0:
        if current == '|':
            floodfillMap[currentPos[0] * 3 - 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1 + 1][currentPos[1] * 3 + 1] = 1
        elif current == 'L':
            floodfillMap[currentPos[0] * 3 - 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1 + 1] = 1
        elif current == 'J':
            floodfillMap[currentPos[0] * 3 - 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 - 1 + 1] = 1
        current = up
        currentPos = [currentPos[0] - 1, currentPos[1]]
        movedTo = "up"
        direction = 2 # came from down
    elif (current == 'F' or current == 'L' or current == '-') and (right == 'J' or right == '7' or right == '-') and direction != 1:
        if current == 'F':
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1 + 1][currentPos[1] * 3 + 1] = 1
        elif current == 'L':
            floodfillMap[currentPos[0] * 3 - 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1 + 1] = 1
        elif current == '-':
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 - 1 + 1] = 1
        current = right
        currentPos = [currentPos[0], currentPos[1] + 1]
        movedTo = "right"
        direction = 3 # came from left
    elif (current == '|' or current == '7' or current == 'F') and (down == '|' or down == 'L' or down == 'J') and direction != 2:
        if current == '|':
            floodfillMap[currentPos[0] * 3 - 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1 + 1][currentPos[1] * 3 + 1] = 1
        elif current == '7':
            floodfillMap[currentPos[0] * 3 + 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 - 1 + 1] = 1
        elif current == 'F':
            floodfillMap[currentPos[0] * 3 + 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1 + 1] = 1
        current = down
        currentPos = [currentPos[0] + 1, currentPos[1]]
        movedTo = "down"
        direction = 0 # came from up
    elif (current == 'J' or current == '7' or current == '-') and (left == 'F' or left == 'L' or left == '-') and direction != 3:
        if current == 'J':
            floodfillMap[currentPos[0] * 3 - 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 - 1 + 1] = 1
        elif current == '7':
            floodfillMap[currentPos[0] * 3 + 1 + 1][currentPos[1] * 3 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 - 1 + 1] = 1
        elif current == '-':
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 - 1 + 1] = 1
            floodfillMap[currentPos[0] * 3 + 1][currentPos[1] * 3 + 1 + 1] = 1
        current = left
        currentPos = [currentPos[0], currentPos[1] - 1]
        movedTo = "left"
        direction = 1 # came from right
    # print(f"moved to {current} in the direction {movedTo}")

    # counter += 1

# next part will add a manual space where there are 2 adjacent but nonconnected pipes

# current = |, 7, or F and adjacent = |, L, or J: down connection
# current = |, L, or J and adjacent = |, 7, or F: up connection
# current = F, L, or - and adjacent = J, 7, or -: right connection
# current = J, 7, or - and adjacent = F, L, or -: left connection


m = len(floodfillMap)
n = len(floodfillMap[0]) # dimensions of bitmap for floodfill algo

# hardcode starting point:
# use 8, 8 for examples
x, y = 380, 75

prevC = floodfillMap[x][y] # value of starting point
newC = 2 # value to change to; main loop is 1 so this differentiates it

counter = floodFill(floodfillMap, m, n, x, y, prevC, newC, counter)
# generates answer

for l in floodfillMap:
  print(f"{floodfillMap.index(l)}: {l}")
  # diagnostics

print(counter)





# print(floodfillMap)



