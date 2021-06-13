x = int(input())
y = int(input())

q = 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4
print(q) 