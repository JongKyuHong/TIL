def dfs(index):
    global cnt
    print(array[index])
    for i in range(len(array[index])):
        if array[index][i] != 0:
            cnt += 1
            dfs(array[index][i])
    return 

for test_case in range(int(input())):
    e, n = map(int, input().split())
    array = [[0] for _ in range(e+2)]
    nodes = list(map(int, input().split()))
    cnt = 1
    for i in range(0,e*2,2):
        array[nodes[i]].append(nodes[i+1])
    dfs(n)
    print(f'#{test_case+1} {cnt}')


