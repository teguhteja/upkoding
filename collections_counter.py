def collection(n, a, n1):
    price = 0
    for i in range(n1):
        g = input('').split(' ')
        i1 = get_index(a, g[0])
        if i1 >= 0:
            a.pop(i1)
            price += int(g[1])
    print(price)


def get_index(list_a, w):
    try:
        i = list_a.index(w)
    except ValueError:
        i = -1
    return i


def main():
    n = int(input(''))
    a = input('').split(' ')
    n1 = int(input(''))
    collection(n, a, n1)


if __name__ == '__main__':
    main()
