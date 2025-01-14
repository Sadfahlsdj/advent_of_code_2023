"""
here lies a disgusting chungus hardcode for p1 that i am not proud of
refer to p2 for the better solution which works for both parts
"""

import copy
from itertools import combinations
from functools import cache

@cache
def read_valid_string(line):
    """
    line - string with no ? (all values are valid)
    return - list (ex: [1, 1, 3]) with lengths of # values
    """

    out, temp = [], 0
    for ind, l in enumerate(line):
        if l == '#':
            temp += 1
            if ind == len(line) - 1: # end of line
                out.append(temp)
        else:
            if temp > 0:
                out.append(temp)
            temp = 0

    return out
def all_combos(l):
    # all combos of elements of length 0 to len(l)
    # likely far too inefficient for p2
    out = []
    for i in range(len(l) + 1):
        out.extend(combinations(l, i))

    return out

with open('input.txt') as f:
    spl = [l.strip().split() for l in f.readlines()]

chars, nums_raw = [s[0] for s in spl], [s[1] for s in spl]
nums = [[int(n) for n in nu.split(',')] for nu in nums_raw]

total_p1 = 0
for i in range(len(nums)):
    start_str, ns = [c for c in chars[i]], nums[i]
    q_indices = [i for i, val in enumerate(start_str) if val == '?']
    idxs = [0] * len(q_indices)
    start_str = list(map(lambda x: '.' if x == '?' else x, start_str))
    st = copy.deepcopy(start_str)

    tmp = 0
    combos = all_combos(q_indices)
    for c in combos:
        for char in c:
            start_str[char] = '#'
        total_p1 += (read_valid_string(tuple(start_str)) == ns)
        tmp += read_valid_string(tuple(start_str)) == ns
        start_str = st[:]

    print(f'string: {"".join([c for c in start_str])}, value: {tmp}')

print(total_p1)


