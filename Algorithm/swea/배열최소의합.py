t = int(input())


def dfs(idx, _sum):
    global min_result
    if idx==n:
        if _sum < min_result:
            min_result = _sum
        return
    if _sum >= min_result:
        return
    for i in range(n):
        if use_check[i]:
            use_check[i] = False
            dfs(idx+1, _sum+map_list[idx][i])
            use_check[i] = True


for test_case in range(1,t+1):
    n = int(input())
    map_list = [list(map(int,input().split())) for _ in range(n)]
    use_check = [True for _ in range(n)]
    min_result = 987654321
    dfs(0,0)
    print(f'#{test_case} {min_result}')



