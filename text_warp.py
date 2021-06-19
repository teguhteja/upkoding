# import textwrap


def wrap(string, max_width):
    n = len(string)
    m = n // max_width
    r = ''
    for i in range(m):
        r = r + string[(i * max_width):(i * max_width + max_width)] + '\n'
    r = r + string[m * max_width:n]
    return r


def main():
    string, max_width = input(''), int(input(''))
    result = wrap(string, max_width)
    print(result)


if __name__ == '__main__':
    main()
