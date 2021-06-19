def ddm(n, m):
    for i in range(n):
        for j in range(m):
            print('-', end='')
        print('')


def main():
    n = list(map(int, input('').split(' ')))
    ddm(n[0], n[1])


if __name__ == '__main__':
    main()
