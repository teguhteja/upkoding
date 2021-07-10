def starter(a, b):
    for i in range(a[1]):
        b.insert(0, b.pop(a[0] - 1))
    return ' '.join(b)


def main():
    n = int(input(''))
    for i in range(n):
        a = list(map(int, input('').split(' ')))
        b = input('').split(' ')
        print(starter(a, b))


if __name__ == '__main__':
    main()
