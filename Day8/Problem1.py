from math import gcd

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

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

# print(locations)
locationToStart = -1
for l in locations:
    if l[0] == 'AAA':
        locationToStart = locations.index(l)
current = locations[locationToStart]
counter = 0

found = False
while not found:
    for i in range(len(directions)):
        print(f"current location is {current}, direction is {directions[i]},", end=" ")
        counter += 1
        loc = current[0]
        # print(f"current location is {current}, current direction is {directions[i]}")
        if directions[i] == 'L':
            indexToFind = 1
        elif directions[i] == 'R':
            indexToFind = 2
        print(f"going to {current[indexToFind]}")
        for l in locations:
            if l[0] == current[indexToFind]:
                print(f"found location {l} that has location {current[indexToFind]} with count {counter}")
                current = l
                break
        if current[0] == 'ZZZ':
            found = True
            break


print(counter)


directionsCurrent = directions








