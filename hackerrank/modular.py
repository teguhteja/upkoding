def get_mod(a, b, m):
    for i in range(1, m+1):
        if (b*i) % m == a:
            return i
    return -1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
        # raise Exception('modular inverse does not exist')
    else:
        return x % m


def main():
    m, t = 1, 1
    lr = []
    while m != 0 and t != 0:
        n = list(map(int, input('').split(' ')))
        m = n[0]
        t = n[1]
        for i in range(t):
            a = input('').split(' ')
            a[0], a[2] = int(a[0]), int(a[2])
            if a[1] == '+':
                lr.append((a[0] + a[2]) % m)
            if a[1] == '-':
                lr.append((a[0] - a[2]) % m)
            if a[1] == '*':
                lr.append((a[0] * a[2]) % m)
            if a[1] == '/':
                mod = modinv(a[2], m)
                r = -1 if mod == -1 else ((a[0] % m) * mod) % m
                lr.append(r)
    for i in range(len(lr)):
        print(lr[i])


if __name__ == "__main__":
    main()
    # print(modinv(5, 3))
    # print(((1 % 1000) * modinv(998, 1000)) % 1000)
