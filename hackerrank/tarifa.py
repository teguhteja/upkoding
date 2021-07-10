max = int(input())
n = int(input())
r = 0
for _ in range(n):
    r = r + max - int(input())
print(r+max)