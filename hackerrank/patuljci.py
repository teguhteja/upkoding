d = []
for _ in range(9):
    d.append(int(input()))
is_break = False
for i in range(9):
    for j in range(8):
        d1 = d.copy()
        d1.pop(i)
        d1.pop(j)
        # print(d1)
        if(sum(d1) == 100):
            for k in range(7):
                print(d1[k]) 
            is_break = True
        if is_break:
            break
    if is_break:
        break 
