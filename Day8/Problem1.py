from math import gcd

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

directions = lines[0] # 281 length
locations = []

for l in lines[2:]:
    location = l[0:3]
    left = l[7:10]
    right = l[12:15]
    locations.append([location, left, right]) # each element is an array of (current, left, right)

for l in locations:
    if l[0] == 'AAA':
        locationToStart = locations.index(l)
current = locations[locationToStart] # makes sure i start in the right spot(IMPORTANT!!)
counter = 0

found = False
while not found:
    for i in range(len(directions)):
        print(f"current location is {current}, direction is {directions[i]},", end=" ") # diagnostic
        counter += 1 # output counting
        loc = current[0] # will be the current location
        # print(f"current location is {current}, current direction is {directions[i]}")
        if directions[i] == 'L':
            indexToFind = 1
        elif directions[i] == 'R': # decides which place to go to based on the current direction
            indexToFind = 2
        print(f"going to {current[indexToFind]}")
        for l in locations:
            if l[0] == current[indexToFind]: # searches for the target location
                print(f"found location {l} that has location {current[indexToFind]} with count {counter}")
                current = l
                break # saves a little bit of speed
        if current[0][2] == 'Z': # same as current[0]=ZZZ, this was done to help with p2
            found = True
            break

print(counter)








