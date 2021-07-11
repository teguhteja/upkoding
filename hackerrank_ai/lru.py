
BLOCKNUMBER = 4


# Download Data
def loadData():
    F = open('data_lru')
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


usedBlock = []
n = 0
dict_n = {}


def loadNextPage(memory, page):
    global n

    if page in memory:
        memory.remove(page)
        memory.append(page)
    else:
        n += 1
        if len(memory) < BLOCKNUMBER:
            memory.append(page)
        else:
            memory.pop(0)
            memory.append(page)
    count_num(memory)
    return memory


data = loadData()
seq = 1
for i in data:
    usedBlock = loadNextPage(usedBlock, i)
    print(f'{seq}th : {usedBlock}')
    seq += 1

print(f'The data are {data}')
print(f'The number of page faults is {n}')
print(f'count : {dict_n}')
