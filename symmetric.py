n = int(input())
my_set = 1
while(n!=0):
    clown = []
    mid = n//2 + 1 if n % 2 == 1 else n//2
    for i in range(n):
        clown.append(input())
    print(f'SET {my_set}')
    my_set += 1 
    for i in range(n):
        index = 2 * i if i < mid else n - (2 * (i-mid) +1 ) if n % 2 == 0 else n - ( 2 * (i-(mid-1))) 
        print(clown[index])
    n = int(input())