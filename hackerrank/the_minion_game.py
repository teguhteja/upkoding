def minion_game(s):
    # s = input()

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)
        # print(f'{s[i]} - {kevsc} - {stusc}')

    if kevsc > stusc:
        print(f"Kevin {kevsc}")
    elif kevsc < stusc:
        print(f"Stuart {stusc}")
    else:
        print("Draw")


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input('')
    s = 'BANANAS'
    minion_game(s)
    # fptr.write(result + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
