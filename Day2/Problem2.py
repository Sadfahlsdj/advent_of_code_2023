with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

index = 1
total = 0

for l in lines:
    l = l.split(":",1)[1].rstrip()

    redArray, blueArray, greenArray = [0], [0], [0]
    red, green, blue = 0, 0, 0

    for i in range(len(l)):
        if l[i] == ';' or i == len(l) - 1:
            # print(f"red = {red}, green = {green}, blue = {blue} on index {index}")
            redArray.append(red)
            greenArray.append(green)
            blueArray.append(blue)

            red, green, blue = 0, 0, 0

        if l[i].isnumeric():
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
    redMax = max(redArray)
    greenMax = max(greenArray)
    blueMax = max(blueArray)

    power = redMax * greenMax * blueMax
    print(f"max red, green, and blue for index {index} are {redMax}, {blueMax}, {greenMax}, and total power is {power}")

    # not needed, just for logging purposes
    total += power
    index += 1

print(total)