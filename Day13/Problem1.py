from numpy import ndarray

def column(index, li):
    returnme = []
    for l in li:
        returnme.append(l[index])
    return returnme

with open('example.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0
formationCount = 1
for l in lines:
    # print(l)
    if l == '':
        formationCount += 1
        # print(f"line {lines.index(l)} is all space")

formations = [[]]
formations.append([''])

i = 0
for l in lines:
    if l == '' and lines.index(l) != len(lines) - 1 :
        formations.append([''])
        i += 1
    formations[i].append(l)

# next few lines are due to terrible input parsing, makes each formation array what it should be
del formations[len(formations) - 1]

for i in range(1, len(formations)):
    del formations[i][0]
    del formations[i][0]

for f in formations:
    for i in range(len(f) - 1):
        horizontalMatch = True
        for j in range(i):
            if f[i - j] != f[i + j + 1]:
                horizontalMatch = False
        if horizontalMatch == True:
            total += (i + 1) * 100
            print(f"horizontal match found with {i+1} lines above line of symmetry")
    print(' ')



