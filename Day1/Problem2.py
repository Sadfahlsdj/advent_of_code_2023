


def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    total = 0
    index = 1

    for l in lines:
        first = 0
        last = 0
        for i in range(len(l) + 1):
            if l.find('one') == i or l.find('1') == i:
                first = 1
                # print("found one first", end=" ")
                break
            if l.find('two') == i or l.find('2') == i:
                first = 2
                break
            if l.find('three') == i or l.find('3') == i:
                first = 3
                break
            if l.find('four') == i or l.find('4') == i:
                first = 4
                break
            if l.find('five') == i or l.find('5') == i:
                first = 5
                break
            if l.find('six') == i or l.find('6') == i:
                first = 6
                break
            if l.find('seven') == i or l.find('7') == i:
                first = 7
                break
            if l.find('eight') == i or l.find('8') == i:
                first = 8
                break
            if l.find('nine') == i or l.find('9') == i:
                first = 9
                break
            if l.find('zero') == i or l.find('0') == i:
                first = 0
                break
        for i in reversed(range(len(l) + 1)):
            if l.rfind('one') == i or l.rfind('1') == i:
                last = 1
                # print("found one", end=" ")
                break
            if l.rfind('two') == i or l.rfind('2') == i:
                last = 2
                break
            if l.rfind('three') == i or l.rfind('3') == i:
                last = 3
                break
            if l.rfind('four') == i or l.rfind('4') == i:
                last = 4
                break
            if l.rfind('five') == i or l.rfind('5') == i:
                last = 5
                break
            if l.rfind('six') == i or l.rfind('6') == i:
                last = 6
                break
            if l.rfind('seven') == i or l.rfind('7') == i:
                last = 7
                break
            if l.rfind('eight') == i or l.rfind('8') == i:
                last = 8
                break
            if l.rfind('nine') == i or l.rfind('9') == i:
                last = 9
                break
            if l.rfind('zero') == i or l.rfind('0') == i:
                last = 0
                break

        addme = int(first) * 10 + int(last)
        print(index, " ", addme)
        total += addme

        index += 1

    print(total)


if __name__ == '__main__':
    main()


