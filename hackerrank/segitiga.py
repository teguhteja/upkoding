def segitiga(number):
    t = int(number/2)
    for i in range(number):
        start = t if i == 0 else int(t - i / 2)
        end =  t if i == 0 else t + i / 2
        for j in range(number):
            if start <= j <= end:
                if i % 2 == 1:
                    print(' *', end='')
                else:
                    print('* ', end='')
            else:
                print('  ', end='')
        print() 
        # print(f'{start, end, i%2}')

segitiga(11)