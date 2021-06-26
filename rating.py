n = input().split()
s = sum(int(input()) for _ in range(int(n[1])))
print( f'{(s + (int(n[0])-int(n[1]))*-3)/int(n[0])} {(s + (int(n[0])-int(n[1]))*3)/int(n[0])}')