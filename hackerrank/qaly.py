n = int(input())
p = 0.0
for _ in range(n):
    i = input().split(' ')
    p += float(i[0])*float(i[1])
print(p)