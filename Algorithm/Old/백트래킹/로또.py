from itertools import combinations

while 1:
    array = list(map(int,input().split()))
    k = array[0]
    if k == 0:
        break
    s = array[1:]
    res = list(combinations(s,6))
    for i in res:
        print(*i)
    print()
