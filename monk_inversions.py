def mi():
    n = int(input())
    matrix = []
    for i in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
        # print(matrix)
    c = 0
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i <= p and j <= q:
                        if matrix[i][j] > matrix[p][q]:
                            c += 1
    return c


def main():
    t = int(input(''))
    for i in range(t):
        print(mi())


if __name__ == '__main__':
    main()
