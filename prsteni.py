import math as m

def prsteni():
    n = int(input(''))
    r = list(map(int, input('').split(' ')))
    for i in range(1,n):    
        g = m.gcd(r[0],r[i])
        print(f'{r[0]//g}/{r[i]//g}')

if __name__ == '__main__':
    prsteni()