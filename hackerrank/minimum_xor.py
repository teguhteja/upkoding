def starter(n, arr):
    ans = float('inf')
    # Sort the array
    arr.sort()
    # Traverse the array arr[]
    for i in range(n - 1):
        # Compare and Find the minimum
        # XOR value of an array.
        ans = min(ans, arr[i] ^ arr[i + 1])
    # Return the final answer
    return str(ans)


def main():
    n = int(input(''))
    for _ in range(n):
        a = int(input(''))
        b = list(map(int, input('').split(' ')))
        print(starter(a, b))


if __name__ == '__main__':
    main()
