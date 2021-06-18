def main():
    n = list(map(int, input('').split(' ')))
    p = n[2]-1-n[1]
    p = 1 if p == 0 else p
    print(p)


if __name__ == '__main__':
    main()
