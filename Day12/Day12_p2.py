from functools import cache

with open('input.txt') as f:
    spl = [l.strip().split() for l in f.readlines()]

chars, nums_raw = [s[0] for s in spl], [s[1] for s in spl]
nums = [[int(n) for n in nu.split(',')] for nu in nums_raw]

def valid(spring, records):
    return (records[0] <= len(spring) and '.' not in spring[:records[0]]
            and (records[0] == len(spring) or spring[records[0]] != '#'))

@cache # using imported memo cause im lazy
def get_valid_combos(spring, records):
    if not records:
        if '#' in spring:
            return 0
        return 1

    if not spring:
        if not records:
            return 1
        return 0

    total_combos = 0
    if spring[0] in ['.', '?']:
        total_combos += get_valid_combos(spring[1:], records)

    if spring[0] in ['#', '?']:
        if valid(spring, records):
            total_combos += get_valid_combos(spring[records[0] + 1:], records[1:])

    return total_combos


# p1
total_p1 = sum([get_valid_combos(chars[i], tuple(nums[i])) for i in range(len(nums))])
print(total_p1)

# p2
nums_p2 = [n * 5 for n in nums]
chars_p2 = [(c + '?') * 4 + c for c in chars]

total_p2 = sum([get_valid_combos(chars_p2[i], tuple(nums_p2[i])) for i in range(len(nums))])
print(total_p2)
