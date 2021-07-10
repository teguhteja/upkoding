import pdb 


def main():
    n = int(input(''))
    a = input('').split(' ')
    l1 = max(map(len, a))
    for i in range((l1 // 5) + 1):
        # p1 = ['' for j in range(n)]
        en = [len(a[l2]) - 5 * i for l2 in range(n)]
        st = [0 if en[m] - 5 < 0 else en[m] - 5 for m in range(n)] 
        a1 = [a[j][st[j]:en[j]] for j in range(n)]
        a1 = list(map(int, a1))
        a2 = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(a1))]
        # pdb.set_trace()
        p1 = [a[a2[k]] for k in range(n)]
        p1 = ' '.join(p1)
        print(p1)


if __name__ == '__main__':
    main()
