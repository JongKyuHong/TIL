def find(r, sum_value):
    global min_value
    for i in range(1, n):
        if not visited[i]:
            break
    else:
        sum_value += graph[r][0]
        min_value = min(min_value, sum_value)
        return min_value

    for i in range(1, n):
        if i != r and not visited[i]:
            visited[i] = 1
            find(i, sum_value+graph[r][i])
            visited[i] = 0

for T in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    min_value = 1001
    visited = [0] * n
    sum_value = 0
    find(0, sum_value)
    print(f'#{T+1} {min_value}')