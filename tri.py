

def my_op(a, b, c):
    if a+b == c:
        return f'{a}+{b}={c}'
    elif a-b == c:
        return f'{a}-{b}={c}'
    elif a*b == c:
        return f'{a}*{b}={c}'
    elif a//b == c:
        return f'{a}/{b}={c}'
    elif a==b+c:
        return f'{a}={b}+{c}'
    elif a==b-c:
        return f'{a}={b}-{c}'
    elif a==b*c:
        return f'{a}={b}*{c}'
    elif a==b/c:
        return f'{a}={b}/{c}'

def tri():
    n = list(map(int, input('').split(' ')))
    print(my_op(n[0], n[1], n[2]))

if __name__ == '__main__':
    tri()