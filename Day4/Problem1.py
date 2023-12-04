with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

for l in lines:
    useless, useful = l.split(':') # gets rid of the "card 1:"
    useful = useful.rstrip() # leading/ending spaces, newlines gone
    # print(useful)
    points = 0.5
    winning, held = useful.split('|') # splits into winning & held lists

    winningNumbers = winning.split(' ')
    heldNumbers = held.split(' ') # self-explanatory

    # print(f"winning numbers = {winningNumbers}")
    # print(f"held numbers = {heldNumbers}")

    for n in winningNumbers:
        for m in heldNumbers:
            if n == m and n != '': #for some reason there are a lot of extra spaces
                # so the winning/held arrays have a lot of elements that are just nothing
                points *= 2
                print('doubled points')

    if points == 0.5:
        pass
    else:
        total += points


print(total)

