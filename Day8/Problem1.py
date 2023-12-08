with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

directions = lines[0]
locations = []

for l in lines[2:]:
    location = l[0:3]
    left = l[7:10]
    right = l[12:15]

    locations.append([location, left, right])

# print(locations)
current = locations[0]
counter = 0




