with open("input.txt") as f:
    lines = [line.strip() for line in f]

total = 0

steps = lines[0].split(sep=',')
print(steps)

for s in steps:
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current = current % 256

    total += current

print(total)