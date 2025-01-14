with open('example.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

def reflection_equality(orig, reflection, orientation):
    # orientation = 1 for vertical reflections (across rows), 0 for horizontal
    if orientation:
        for i in range(len(orig)):
            if orig[len(orig) - i - 1] != reflection[i]:
                return 0
    else:
        for i in range(len(orig[0])):
            if orig[:][len(orig) - i - 1] != reflection[:][i]:
                return 0

    print(f'orig = {orig}, reflection = {reflection}, orientation = {orientation}')
    return 1
def find_reflection(inp):
    # check horizontal (across rows)
    vert_len = len(inp)
    for i in range(1, vert_len):
        dir = 0 if i < float(vert_len / 2) else 1 # 0 = on top half, 1 = on bottom half
        if not dir:
            # for j in range(i):
            #     print(inp[j])
            # print('reflection')
            # for j in range(i, 2*i):
            #     print(inp[j])
            # print('')

            if reflection_equality(inp[:i], inp[i:2*i], 1):
                return 100 * i
        else:
            diff = vert_len - i
            if reflection_equality(inp[i - diff:i], inp[i:], 1):
                return 100 * i

    # check vertical (across columns)
    hor_len = len(inp[0])
    for i in range(1, hor_len):
        dir = 0 if i < float(hor_len / 2) else 1
        if not dir:
            if reflection_equality(inp[:][:i], inp[:][i:2*i], 0):
                print(f'index = {i}, vertical reflect')
                return i
        else:
            diff = hor_len - i
            print(f'{inp[:][i - diff:i]}\nreflection\n{inp[:][i:]}')
            if reflection_equality(inp[:][i - diff:i], inp[:][i:], 0):
                print(f'index = {i}, vertical reflect')
                return i



sets, temp = [], [] # sets is 3d list, each inner 2d = 1 "set" together
for index, l in enumerate(lines):
    if l != '':
        temp.append(l)
        # print(f'appending line {l}')
    if l == [] or index == (len(lines) - 1): # empty list = empty line in input
        sets.append(temp[:])
        # print(sets)
        temp.clear()

print(find_reflection(sets[0]))








