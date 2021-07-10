import sys


def main():
    n = int(input(''))
    for i in range(n):
        n = int(input(''))
        a = list(map(int, input('').split()))
        dict = {}

        for i in a:
            if(i in dict):
                dict[i] += 1
            else:
                dict[i] = 1

        mini, maxi = sys.maxsize, -sys.maxsize - 1
        v = 0
        for j, i in sorted(dict.items()):
            mini = min(i, mini)
            maxi = max(i, maxi)
            v = -1 if(maxi - mini <= 0) else maxi - mini
            #     print(-1)
            # else:
            #     print(maxi - mini)
        print(str(v))


if __name__ == '__main__':
    main()
