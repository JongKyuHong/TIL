def dfs(index):
    if index > n+1:
        return 0
    if graph[index]:
        return graph[index]
    left = index*2
    right = index*2 +1
    graph[index] = dfs(left) + dfs(right)
    return graph[index]

for test_case in range(int(input())):
    n, m, l = map(int, input().split())
    graph = [0 for _ in range(n+2)]
    for _ in range(m):
        leaf_num, value = map(int, input().split())
        graph[leaf_num] = value
    res = dfs(l)
    print(f'#{test_case+1} {res}')



