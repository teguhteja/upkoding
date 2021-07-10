n = int(input())
t = 0
if n % 2 == 0:
    for _ in range(int(n/2)):
        a = int(input())
        b = int(input())
        t += (a-b)*-1
    print(t)
else:
    print('still running')