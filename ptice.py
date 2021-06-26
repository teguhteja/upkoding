def count_match(a, b):
    return sum(a[i] == b[i] for i in range(len(a)))


def main():
    n = int(input(''))
    m = input('')
    a = 'ABC'*((n//3)+1)
    b = 'BABC'*((n//4)+1)
    c = 'CCAABB'*((n//6)+1)
    a_c = count_match(m, a)
    b_c = count_match(m, b)
    c_c = count_match(m, c)
    m_c = max(a_c, b_c, c_c)
    print(m_c)
    if m_c == a_c:
        print('Adrian')
    if m_c == b_c:
        print('Bruno')
    if m_c == c_c:
        print('Goran')


if __name__ == '__main__':
    main()
