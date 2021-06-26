def main():
    n = int(input(''))
    n1 = 4 * n - 3
    mid_x = n1 // 2
    m = 2 * n - 1
    mid_y = m // 2

    for i in range(m):
        i = i if i <= mid_y else m - i - 1
        p = '-' * n1
        l1 = 2 * i + 1 if i <= mid_y else 2 * (m - 1 - i) + 1
        st = mid_x - 2 * i
        for j in range(l1):
            i1 = st + 2 * j
            j = j if j <= l1 // 2 else l1 - j - 1
            v = 96 + n - j
            p = p[:i1] + chr(v) + p[i1 + 1:]
        print(p)
