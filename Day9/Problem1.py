import sys

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

for l in lines:
    numbers = [int(a) for a in l.split()]
    # print(f"size of this line is {len(numbers)}")

    zerod = False # true once every value is 0

    rows, cols = len(numbers), len(numbers) + 1
    differences = [[sys.maxsize for i in range(cols)] for j in range(rows)]

    differences[0] = numbers
    elementNumbers = []
    i = 0 # used to keep track of which layer of differences we are on, layer 0 is the initial array
    # this while loop generates all differences
    while not zerod:
        elementNumbers.append(sum(1 for n in differences[i] if n != sys.maxsize))
        print(f"{differences[i]}, elementNumber is {elementNumbers[i]}")
        # print(f"{elementNumber} elementnumber")
        i += 1
        for j in range(1, elementNumbers[i-1]):
            differences[i][j-1] = (differences[i-1][j] - differences[i-1][j-1])
        if all([b == 0 for b in differences[i] if b != sys.maxsize]):
            zerod = True
            differences[i] = [0 if x == sys.maxsize else x for x in differences[i]]
            print(differences[i])
            print(f"index {lines.index(l)} of the input has been zerod")


    numberToAdd = -1
    currentAddition = []
    currentAddition.append(0)
    # this while loop goes in reverse and generates the next number
    for i in reversed(range(1, len(elementNumbers) + 1)):

        indexToUse = 0
        # finds first instance of sys.maxsize (first placeholder number, which can be overwritten)
        for n in differences[i-1]:
            if n == sys.maxsize:
                indexToUse = differences[i-1].index(n)
        # print(f"{differences[i-1]}, {indexToUse}")
        """print(currentAddition[len(currentAddition) - 1])
        print(differences[i - 1][indexToUse - 1])
        print(currentAddition[len(currentAddition) - 1])"""
        currentAddition.append(currentAddition[len(currentAddition) - 1] + differences[i-1][indexToUse - 1])
        # print(currentAddition)
    total += currentAddition[len(currentAddition) - 1]
    print(f"adding {currentAddition[len(currentAddition) - 1]}, total is now {total}")


print(total)

