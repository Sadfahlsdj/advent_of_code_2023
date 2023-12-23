with open("example.txt") as f:
    lines = [line.strip() for line in f]

startPos = []
steps = 6 # number of loops, 6 for testing, 64 for actual problem

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            startPos = [i, j]
            lines[i] = lines[i].replace('S', '.')

print(lines)
print(startPos)

# even number of steps will just draw concentric rings with "radius" 2, 4, 6... etc on a blank board
# not as simple as that because rocks can make it take more turns to reach certain blocks