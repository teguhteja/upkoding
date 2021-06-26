def ddm(n, m):
    mid = n // 2
    for i in range(n):
        for j in range(n):  # height
            if i == mid:
                p = '-' * 3 if j < mid - 1 else '-WELCOME-'
                print(p, end='')
                if j == mid - 1:
                    print('-' * (3 * (n - mid - 2)), end='')
                    break
            elif i < mid:
                if j >= mid - i and mid + i >= j:
                    p = '.|.'
                else:
                    p = '-' * 3
                print(p, end='')
            else:
                if j >= i - mid and n - (i - mid) > j:
                    p = '.|.'
                else:
                    p = '-' * 3
                print(p, end='')
        print('')


def main():
    n = list(map(int, input('').split(' ')))
    ddm(n[0], n[1])


if __name__ == '__main__':
    main()
