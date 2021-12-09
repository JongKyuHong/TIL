def dfs(index,res):
    if index == n:
        global result
        if result < res:
            result = res
        return
    if res < result:
        return
    for i in range(n):
        if not visited[i] and test_list[index][i] != 0:
            visited[i] = 1
            res2 = res*(test_list[index][i]*0.01)
            dfs(index+1, res2)
            visited[i] = 0
    

for test_case in range(int(input())):
    n = int(input())
    test_list = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    result = 0
    dfs(0,1)
    print(f'#{test_case+1} {result*100:.6f}')