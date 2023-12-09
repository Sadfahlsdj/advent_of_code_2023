# IMPORTANT, READ:
# p1 and p2 solutions differ by literally 1 line - it's commented below, can ctrl+f "p1 line"

import sys

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

for l in lines:
    numbers = [int(a) for a in l.split()]

    zerod = False # true once every value is 0

    rows, cols = len(numbers), len(numbers) + 1
    differences = [[sys.maxsize for i in range(cols)] for j in range(rows)]
    # initializes all values to sys.maxsize to use as a placeholder
    # functional but probably inefficient methodology

    differences[0] = numbers # sets first line to input line
    elementNumbers = [] # used to keep track of how many actual values are on each line

    i = 0 # used to keep track of which layer of differences we are on, layer 0 is the initial array
    # this while loop generates all differences
    while not zerod:
        elementNumbers.append(sum(1 for n in differences[i] if n != sys.maxsize)) # generates elementNumbers
        print(f"{differences[i]}, elementNumber is {elementNumbers[i]}")
        # print(f"{elementNumber} elementnumber")
        i += 1
        for j in range(1, elementNumbers[i-1]):
            differences[i][j-1] = (differences[i-1][j] - differences[i-1][j-1]) # generates differences
        if all([b == 0 for b in differences[i] if b != sys.maxsize]):
            # if every actual value is zero, end the loop
            zerod = True
            differences[i] = [0 if x == sys.maxsize else x for x in differences[i]]
            print(differences[i])
            print(f"index {lines.index(l)} of the input has been zerod")


    numberToAdd = -1 # placeholder
    currentAddition = [] # will be used to calculate a running total of the value thats being added
    currentAddition.append(0) # initial value to add (the bottom layer of differences is all zeroes)
    # this while loop goes in reverse and generates the next number
    for i in reversed(range(1, len(elementNumbers) + 1)):

        indexToUse = 0
        # finds first instance of sys.maxsize (first placeholder number, which can be overwritten)
        for n in differences[i-1]:
            if n == sys.maxsize:
                indexToUse = differences[i-1].index(n)
        # print(f"{differences[i-1]}, {indexToUse}")

        # p1 line:
        # currentAddition.append(currentAddition[len(currentAddition) - 1] + differences[i-1][indexToUse - 1])
        # p2 line:
        currentAddition.append(differences[i - 1][0] - currentAddition[len(currentAddition) - 1])
        # currentAddition uses the most recent value in the array plus/minus the last/first value in the next differences array
        print(currentAddition)
    total += currentAddition[len(currentAddition) - 1]
    print(f"adding {currentAddition[len(currentAddition) - 1]}, total is now {total}")


print(total)

