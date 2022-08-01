for _ in range(int(input())):
    n, m = map(int,input().split())
    array = list(map(int, input().split()))
    idx = list(range(len(array)))
    idx[m] = 'target'
    cnt = 0
    while 1:
        if array[0] == max(array):
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                idx.pop(0)
                array.pop(0)
        else:
            idx.append(idx.pop(0))
            array.append(array.pop(0))