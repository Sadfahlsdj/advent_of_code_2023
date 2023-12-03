with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0
index = 1

redLimit, greenLimit, blueLimit = 12, 13, 14 # so I don't have to remember

for l in lines:
    failed = False # since I can't break a nested loop
    red, green, blue = 0, 0, 0
    l = l.split(":",1)[1].rstrip() # man what even the shit does this do I forgot
    for i in range(len(l)):
        if l[i] == ';' or i == len(l) - 1: # on each semicolon, check if failed, if not, reset all values
            if red > redLimit or blue > blueLimit or green > greenLimit:
                failed = True
                print(f"red = {red}, green = {green}, blue = {blue} on index {index} when it failed")

            else:
                print(f"red = {red}, green = {green}, blue = {blue} on index {index} when one individual game passed")
                red, green, blue = 0, 0, 0
        if l[i].isnumeric():
            # constructs numbers from digits
            # hardcoded because they only go up to 2 digits
            if l[i+1].isnumeric():
                if l[i + 3] == 'r':
                    red += int(l[i]) * 10
                elif l[i + 3] == 'b':
                    blue += int(l[i]) * 10
                elif l[i + 3] == 'g':
                    green += int(l[i]) * 10
            else:
                if l[i+2] == 'r':
                    red += int(l[i])
                elif l[i+2] == 'b':
                    blue += int(l[i])
                elif l[i+2] == 'g':
                    green += int(l[i])

    if not failed:
        total += index # adds if no check failed on this row
        # print(f"added {index} to total")
    index += 1

print(total)