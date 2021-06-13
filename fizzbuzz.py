a = list(map(int, input().split(' ')))
for i in range(1, a[2]+1):
    b = 'FizzBuzz' if i % a[0] == 0 and i % a[1] == 0 else 'Fizz' if i % a[0] == 0 else 'Buzz' if i % a[1] == 0 else i
    print(b)