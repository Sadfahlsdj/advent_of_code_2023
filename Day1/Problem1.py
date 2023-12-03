


def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    total = 0

    for l in lines:
        first = 0
        last = 0
        for c in l:
            if c.isdigit():
                first = c
                break
        for c in reversed(l):
            if c.isdigit():
                last = c
                break

        addme = int(first) * 10 + int(last)
        print(addme)
        total += addme

    print(total)


if __name__ == '__main__':
    main()


