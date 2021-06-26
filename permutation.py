from itertools import permutations
s = input().split(' ')

b = list(permutations(s[0], int(s[1])))
b.sort()
for b1 in b:
    print(''.join(b1))
