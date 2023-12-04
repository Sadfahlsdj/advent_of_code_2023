with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

cardAmount = len(lines)
cardAmounts = [1] * cardAmount


for i in range(len(lines)):
    useless, useful = lines[i].split(':') # gets rid of the "card 1:"
    useful = useful.rstrip() # leading/ending spaces, newlines gone
    # print(useful)
    winning, held = useful.split('|') # splits into winning & held lists

    winningNumbers = winning.split(' ')
    heldNumbers = held.split(' ') # self-explanatory

    # print(f"winning numbers = {winningNumbers}")
    # print(f"held numbers = {heldNumbers}")

    addCoefficient = 1 # keeps track of what index to add cards to
    for n in winningNumbers:
        for m in heldNumbers:
            if n == m and n != '': # for some reason there are a lot of extra spaces
                # so the winning/held arrays have a lot of elements that are just nothing

                for j in range(cardAmounts[i]): # addition has to be repeated per copy of that card
                    if i + addCoefficient < len(cardAmounts): # avoids oob issues
                        cardAmounts[i + addCoefficient] += 1

                addCoefficient += 1 # increments after copies are added to one card
    # print("")
    total += cardAmounts[i]


print(total)

