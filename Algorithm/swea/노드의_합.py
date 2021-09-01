def dfs(idx):
    if idx > n+1: return 0
    if sum_field[idx]: return sum_field[idx]
    left = idx*2
    right = idx*2 + 1
    sum_field[idx] = dfs(left) + dfs(right)
    return sum_field[idx]

for test_case in range(int(input())):
    n, m, l = map(int, input().split())
    sum_field = [0 for _ in range(n+2)]
    for _ in range(m):
        leaf_num, value = map(int, input().split())
        sum_field[leaf_num] = value
    res = dfs(l)

    print(f'#{test_case+1} {res}')



