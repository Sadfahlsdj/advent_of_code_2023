def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    total = 0

    for l in lines:
        first = 0
        last = 0
        for c in l:
            if c.isdigit(): # find first digit
                first = c
                break
        for c in reversed(l):
            if c.isdigit(): # find last digit
                last = c
                break

        addme = int(first) * 10 + int(last)
        print(addme)
        total += addme # constructs & adds number from digits

    print(total)


if __name__ == '__main__':
    main()


