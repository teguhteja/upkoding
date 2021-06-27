
def test_num():
    mx = 1000000009
    for i in range(mx):
        b = 0 if i == 1 else (i - 1) * pow(10, i - 2)
        a = pow(10, i) - b % mx
        print(f'{i} -- {len(str(a))}')


def starter(n, a, b):
    pass


def main():
    mx = 1000000009
    t = int(input(''))
    for _ in range(t):
        i = int(input(''))
        b = 0 if i == 1 else (i - 1) * pow(10, i - 2)
        a = pow(10, i) - b % mx
        print(str(a))


if __name__ == '__main__':
    main()
