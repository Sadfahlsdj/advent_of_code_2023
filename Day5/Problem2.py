import re
import sys

with open('example.txt') as f:
    lines = [line.rstrip() for line in f]

maps = [[0 for i in range(1)] for j in range(7)]
# soil, fertilizer, water, light, temp, humidity, location respectively

partitions = []
for i in range(1, len(lines)):
    for match in re.finditer(':', lines[i]):
        partitions.append(i) # finds all instances of :

# seeds = lines[1].split() # seeds are different, they don't go in the 2d array
seeds = lines[1].split()

for i in range(len(partitions) - 1):
    maps[i] = lines[partitions[i] + 1:partitions[i + 1] - 1]
    # separates into the categories specified by problem

maps[6] = lines[partitions[6] + 1:]
# hardcoding last category(humidity to location) to avoid oob issues

values = [[0 for i in range(3)] for j in range(7)] # obscene 3d list that stores all values
# category, line number within category, and [destination, source, range] respectively

for i in range(len(maps)):
    for l in maps[i]:
        dest, src, rng = l.split(' ') # splits by spaces into the 3 target values
        dest, src, rng = int(dest), int(src), int(rng) # they're originally strings
        values[i].append([dest, src, rng]) # appends a triple to be used later

cv = seeds # stands for currentValue, name was just too long
for i in range(len(cv)):
    cv[i] = int(cv[i]) # they are strings before this

for i in range(len(values)):
    del values[i][0:3]
    # due to using append instead of reassigning values
    # and due to how I initialized values
    # there's an extra three 0s at the beginning of each element, this removes it

# treat currentValues array as a set of ranges
# each pair is starting value, range

print(cv)

# dest + initial - source, min(c[k+1], range)
# after first iteration it should be: [(50+79-52) min(14, 48) 50+(55-52) min(13, 48)]
# [77, 14, 53, 13]

"""
79 14 55 13

50 98 2
52 50 48
-----------------

77, 14, 53, 13
0 15 37
37 52 2
39 0 15

77, 14, 38, 2
"""
for i in range(len(values)): # iterate over each map
    changed = [False for z in range(len(cv))]
    # if k, k+1 are the indices of a pair, just set both to True if that range was changed
    for j in range(len(values[i])): # iterate over each line within the map
        dest, src, rng = values[i][j][0], values[i][j][1], values[i][j][2] # for my own benefit
        for k in range(0, int(len(cv)) - 1, 2):
            # currentValues[k] will be each starting value of a range
            if cv[k] + cv[k + 1] >= src and src + rng >= cv[k]:
                if not changed[k]: # avoids double changing within a category
                    print(f"changed on dest, src, rng {dest}, {src}, {rng} with initial & range {cv[k]}, {cv[k+1]}")
                    changed[k], changed[k+1] = True, True
                    cv[k] = dest + cv[k] - src # sets first value in the range
                    tmp2 = min(cv[k+1], rng)
                    # cv[k] = cv[k] + src - dest
                    # cv[k] = max(src, cv[k]) - abs(src - dest)
                    cv[k + 1] = tmp2 # sets the actual range
            else:
                print(f"not changed on dest, src, rng {dest}, {src}, {rng}")
# 82, 84, 84, 84, 77, 45, 46, 46

    print(cv)

minStart = cv[0]
for k in range(0, int(len(cv)) - 1, 2):
    if cv[k] < minStart:
        minStart = cv[k]

print(minStart)