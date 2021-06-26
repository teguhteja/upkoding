n = int(input(''))
le = len(bin(n)) - 1
for i in range(1, n + 1):
    d = str(i).rjust(le - 1)
    o = oct(i).replace('0o', '').rjust(le)
    h = hex(i).replace('0x', '').rjust(le).upper()
    b = bin(i).replace('0b', '').rjust(le)
    p = d + '' + o + '' + h + '' + b
    print(p)
