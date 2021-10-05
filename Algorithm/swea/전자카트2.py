import itertools

def dfs(target):
    val = 0
    now = 0
    for i in range(length):
        val += array[now][int(target[i])]
        now = int(target[i])
    val += array[now][0]
    return val


for test_case in range(int(input())):
    n = int(input())
    a = list(map(str,range(1,n)))
    _list = list(map(''.join, itertools.permutations(a)))
    array = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')
    length = n-1
    for i in range(len(_list)):
        val = dfs(_list[i])
        if res > val:
            res = val
    print(f'#{test_case+1} {res}')