import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

maps = [[0 for i in range(1)] for j in range(7)]
# soil, fertilizer, water, light, temp, humidity, location respectively

partitions = []
for i in range(1, len(lines)):
    for match in re.finditer(':', lines[i]):
        partitions.append(i) # finds all instances of :

# seeds = lines[1].split() # seeds are different, they don't go in the 2d array
seedInput = lines[1].split()
for i in range(len(seedInput)):
    seedInput[i] = int(seedInput[i])
seeds = []

j = 0
while j < len(seedInput) - 1:
    print('a')
    # seedInput[i], seedInput[i+1] = int(seedInput[i]), int(seedInput[i+1])
    for j in range(seedInput[j+1]):
        seeds.append(seedInput[i] + j)
    i += 2


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

currentValues = seeds
for i in range(len(currentValues)):
    currentValues[i] = int(currentValues[i]) # they are strings before this



for i in range(len(values)):
    del values[i][0:3]
    # due to using append instead of reassigning values
    # and due to how I initialized values
    # there's an extra three 0s at the beginning of each element, this removes it

for i in range(len(values)): # iterate over each map
    changed = [False for z in range(len(currentValues))] # see conditional below
    for j in range(len(values[i])): # iterate over each line within the map
        dest, src, rng = values[i][j][0], values[i][j][1], values[i][j][2] # for my own benefit
        for k in range(len(currentValues)): # iterate over each currently tracked value
            # print(currentValues[k])
            if currentValues[k] < src + rng and currentValues[k] >= src:
                if not changed[k]: # avoids double changing within a category
                    changed[k] = True
                    # print(f"found source {currentValues[k]}, with source and range {src}, {rng} on map number {i+1}, and changed it to {dest + currentValues[k] - src}")
                    currentValues[k] = dest + currentValues[k] - src
            else:
                currentValues[k] = currentValues[k] # honestly not needed, just for clarity

    print(currentValues)

print(min(currentValues))