t = int(input())
king_array = []
for _ in range(t):
    array = []
    n,m = map(int,input().split())
    for _ in range(m):
        array.append(list(map(int,input().split())))
    array.sort(key=lambda x : x[1])
    new_array = [0] * (n+1)
    flag = 0
    cnt = 0
    while array:
        a,b = array.pop(0)
        for i in range(a,b+1):
            if new_array[i] == 0:
                cnt += 1
                new_array[i] = 1
                break
    print(cnt)