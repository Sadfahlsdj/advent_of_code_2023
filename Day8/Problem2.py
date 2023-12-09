from math import gcd
from functools import reduce

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def lcm(numbers):
    return reduce(lambda x, y: x * y // gcd(x, y), numbers, 1)

# everything that ends in Z has only one path
# everything that ends in A is unreachable normally

directions = lines[0] # 281 length
locations = []

locationDict = {}

for l in lines[2:]:
    location = l[0:3]
    left = l[7:10]
    right = l[12:15]

    locations.append([location, left, right])
    locationDict.update({location: [left, right]})

# print(locationDict) # key is location, values is an array with [left location, right location]

current = []
ends = []
# print(locations)
locationToStart = -1
for l in locations:
    if l[0][2] == 'A':
        current.append(l)

counter = [0] * len(current)
print(current)
found = [False] * len(current)
print(found)
while not all(f for f in found):
    for i in range(len(directions)):
        for j in range(len(current)):
            if not found[j]:
                # print(f"current location is {current}, direction is {directions[i]},", end=" ")
                counter[j] += 1
                loc = current[j][0]
                # print(f"current location is {current}, current direction is {directions[i]}")
                if directions[i] == 'L':
                    indexToFind = 1
                elif directions[i] == 'R':
                    indexToFind = 2
                # print(f"going to {current[j][indexToFind]}")
                for l in locations:
                    if l[0] == current[j][indexToFind]:
                        # print(f"found location {l} that has location {current[j][indexToFind]} with count {counter}")
                        current[j] = l
                        break
                if current[j][0][2] == 'Z':
                    found[j] = True
                    ends.append(current[j][0])
                    break


print(counter)
print(lcm(counter))

print(ends)

"""
wrong answer:
34324276586199360428040
"""

directionsCurrent = directions








