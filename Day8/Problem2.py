from math import gcd
from functools import reduce

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def lcm(numbers):
    return reduce(lambda x, y: x * y // gcd(x, y), numbers, 1) # for use later

def findZ(currentOriginal, current, counter, directions):
    # pretty much identical to p1 code, probably missing some comments
    found = False
    while not found:
        for i in range(len(directions)):
            # print(f"current location is {current}, direction is {directions[i]},", end=" ")
            counter += 1
            loc = current[0]
            # print(f"current location is {current}, current direction is {directions[i]}")
            if directions[i] == 'L':
                indexToFind = 1
            elif directions[i] == 'R':
                indexToFind = 2
            # print(f"going to {current[indexToFind]}")
            for l in locations:
                if l[0] == current[indexToFind]:
                    # print(f"found location {l} that has location {current[indexToFind]} with count {counter}")
                    current = l
                    break
            if current[0][2] == 'Z':
                found = True
                print(f"original is {currentOriginal} and endpoint is {current} with count {counter}")
                break
    return counter


# everything that ends in Z has only one path
# everything that ends in A is unreachable normally

directions = lines[0] # 281 length
locations = []

for l in lines[2:]:
    location = l[0:3]
    left = l[7:10]
    right = l[12:15]
    locations.append([location, left, right])

# print(locationDict) # key is location, values is an array with [left location, right location]

current = []

for l in locations:
    if l[0][2] == 'A':
        current.append(l) # starts as an array of all "locations" that have current end in a

currentOriginal = current.copy() # used for diagnostics

counter = [0] * len(current) # array of counts, one for each starting location
ends = [['AAA', 'AAA', 'AAA']] * len(current) # used for diagnostics
print(current)
found = [False] * len(current) # one for each starting location
# print(found)


for i in range(len(counter)):
    counter[i] = findZ(currentOriginal[i], current[i], counter[i], directions)
    # updates counter array with each individual count
print(counter)
print(ends)

print(lcm(counter)) # lcm of all individual counts will tell us when every z is concurrently found

"""
wrong answer:
34324276586199360428040
right answer:
15995167053923
"""










