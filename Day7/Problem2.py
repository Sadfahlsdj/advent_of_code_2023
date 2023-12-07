from collections import Counter

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

"""
CURRENT STEPS AFTER P1 COPYPASTE
-changed the 'J' string replacement to 1 to reflect Joker's lowest individual card ranking
-joker logic done by adding the joker count to the highest index and going from there
-if joker is present in the hand, removed the count of the joker and appended a 0
    first is for edge cases where joker is the most common, second is for if every card is joker
-still not working, do tomorrow
-fixed edge case with full house and 2 pair
-re-fixed full house
-re-fixed full house
-current wrong answers: 252486213, 252368364
-fifth time was the charm 252137472 is correct GOD BLESS
"""

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

    ccList = list(cardCounts) # creates list so I can do list operations
    # stands for card count list

    if 'J' in uniqueCards:
        jokerCount = ccList[list(uniqueCards).index('J')]
        if max(ccList) == jokerCount:
            ccList.remove(jokerCount) # removes the joker count if it's the most common
        if jokerCount == 5:
            ccList.append(0) # ccList will be empty after removing jokerCount otherwise
        ccList[ccList.index(max(ccList))] += jokerCount
    else:
        jokerCount = 0

    # maxWithJoker = max(ccList) + jokerCount
    maxWithJoker = max(ccList)
    # since jokerCount is set to 0 if there are no jokers

    # diagnostics
    twoAmount = sum(value == 2 for value in cardCounts)
    print(f"hand, max count, joker count, max count with joker, and amount of two counts are: {hList}, {max(ccList)}, {jokerCount}, {maxWithJoker}, {twoAmount}")
    if maxWithJoker == 5: # 5 of a kind
        values.append([1000000, hands.index(h)])
        # the second element here is the original index of the hand in the hands list
        # will be used for calculation at the end
    elif maxWithJoker == 4: # 4 of a kind
        values.append([100000, hands.index(h)])
    elif maxWithJoker == 3 and 2 in ccList: # full house
        values.append([10000, hands.index(h)])
    elif maxWithJoker == 3: # three of a kind
        values.append([1000, hands.index(h)])
    elif sum(value == 2 for value in cardCounts) == 2: # two pair
        values.append([100, hands.index(h)])
    elif maxWithJoker == 2: # one pair
        values.append([10, hands.index(h)])
    else: # high card
        values.append([1, hands.index(h)])
    # print(values[len(values)-1][0])

for i in range(len(hands)):
    # replaces letter values in hands with values that will compare correctly in string comparison
    hands[i] = hands[i].replace('A', 'Z')
    hands[i] = hands[i].replace('K', 'Y')
    hands[i] = hands[i].replace('Q', 'X')
    hands[i] = hands[i].replace('J', '1') # since j is now joker
    hands[i] = hands[i].replace('T', 'V')

handsChanged = hands.copy() # for use with the sorting



# diagnostics
print("hands & values & bets: ")
print(values)
print(hands)
print(bets)

sortValues(values, handsChanged) # sorts hand values

for v in values:
    total += (len(hands) - v[1]) * bets[values[v[1]][1]]
    # tallies up output
print(total)