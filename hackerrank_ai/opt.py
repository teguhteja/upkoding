import ipdb

BLOCKNUMBER = 4


# Download Data
def loadData():
    F = open('data_opt_2')
    data = F.read().split(' ')
    F.close()
    return data


def count_num(memory):
    global dict_n
    for m in memory:
        if m in dict_n.keys():
            dict_n[m] += 1
        else:
            dict_n[m] = 1


dict_n = {}
usedBlock = []
n = 0


def loadNextPage(memory, page, data):  
    global n
    l1 = []
    if page not in memory:
        n += 1
        if len(memory) < BLOCKNUMBER:
            memory.append(page)

        else:
            for m in memory:
                for i in range(len(data)):
                    if m == data[i]:
                        l1.append(i)
                        break
                    elif i == len(data) - 1 and m != data[i]:
                        # ipdb.set_trace()
                        l1.append(2147483647)
            if len(l1) == 0:
                l1.append(2147483647)
            index = l1.index(max(l1))

            memory.remove(memory[index])
            memory.append(page)
    count_num(memory)
    return memory


data = loadData()
data2 = data.copy()
seq = 1
for i in data:
    data2.remove(i)
    usedBlock = loadNextPage(usedBlock, i, data2)
    print(f'{seq}th : {usedBlock}')
    # print(data2)
    seq += 1

print(f'The data are {data}')
print(f'The number of page faults is {n}')
print(f'count : {dict_n}')
