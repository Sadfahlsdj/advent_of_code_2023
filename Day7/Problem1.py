from collections import Counter

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0
def sortValues(values, handsChanged):
    # letter values in hands have been replaced so the largest values in the problem
    # will be the largest by ascii comparison
    # with slight variations this is just a normal bubblesort
    n = len(values)
    for i in range(n - 1):
        for j in range(0, n-1-i):
            # print(f"comparing {handsChanged[j]} and {handsChanged[j + 1]} with values {values[j][0]} and {values[j+1][0]}")
            if (values[j][0] < values[j+1][0]) or (values[j][0] == values[j+1][0] and handsChanged[j] < handsChanged[j+1]):
                # if equal, compare the deck strings to see which is larger
                # print(f"with respective values {values[j][0]} and {values[j+1][0]}, {handsChanged[j+1]} is bigger")
                values[j], values[j+1] = values[j+1], values[j]
                handsChanged[j], handsChanged[j + 1] = handsChanged[j + 1], handsChanged[j]
        # print(handsChanged)

hands, bets, values = [], [], []
for l in lines:
    hands.append(l.split(' ')[0]) # first section of a line
    bets.append(int(l.split(' ')[1])) # second section of a line

for h in hands:
    hList = list(h)
    uniqueCards = Counter(hList).keys() # contains one of each unique card
    cardCounts = Counter(hList).values() # number of occurrences of each unique card

    if max(cardCounts) == 5: # 5 of a kind
        values.append([1000000, hands.index(h)])
        # the second element here is the original index of the hand in the hands list
        # will be used for calculation at the end
    elif max(cardCounts) == 4: # 4 of a kind
        values.append([100000, hands.index(h)])
    elif 3 in cardCounts and 2 in cardCounts: # full house
        values.append([10000, hands.index(h)])
    elif 3 in cardCounts: # three of a kind
        values.append([1000, hands.index(h)])
    elif sum(value == 2 for value in cardCounts) == 2: # two pair
        values.append([100, hands.index(h)])
    elif max(cardCounts) == 2: # one pair
        values.append([10, hands.index(h)])
    else: # high card
        values.append([1, hands.index(h)])
    # print(values[len(values)-1][0])

for i in range(len(hands)):
    # replaces letter values in hands with values that will compare correctly in string comparison
    hands[i] = hands[i].replace('A', 'Z')
    hands[i] = hands[i].replace('K', 'Y')
    hands[i] = hands[i].replace('Q', 'X')
    hands[i] = hands[i].replace('J', 'W')
    hands[i] = hands[i].replace('T', 'V')

handsChanged = hands.copy() # for use with the sorting

sortValues(values, handsChanged) # sorts hand values

# diagnostics
print("updated values: ")
print(values)
print(hands)
print(bets)

for v in values:
    total += (len(hands) - v[1]) * bets[values[v[1]][1]]
    # tallies up output
print(total)