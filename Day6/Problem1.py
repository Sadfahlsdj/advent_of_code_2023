# FOR P2 I JUST MANUALLY EDITED MY INPUT, THERE IS NO CODE HERE TO DO THAT

import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# end - start + 1
total = 1

times = []
records = []

for match in re.finditer('[0-9]+', lines[0]):
    times.append(int(match.group()))
for match in re.finditer('[0-9]+', lines[1]):
    records.append(int(match.group()))

for i in range(len(times)):
    time = times[i]
    record = records[i]
    low, high = 0, 0
    for j in range(time):
        if (time - j) * j > record:
            low = j
            break
    for j in reversed(range(time)):
        if (time - j) * j > record:
            high = j
            break
    total *= (high - low + 1)

print(total)

