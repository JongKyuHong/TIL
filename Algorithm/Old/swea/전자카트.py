def find(y, sum_value):
    global min_value
    for i in range(1,n):
        if not visited[i]:
            break
    else:
        sum_value += graph[y][0]
        min_value = min(min_value,sum_value)
        return min_value
    for i in range(1,n):
        if i != y and not visited[i]:
            visited[i] = True
            find(i, sum_value+graph[y][i])
            visited[i] = False




for test_case in range(int(input())):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [False] * n
    min_value = 1001
    sum_value = 0
    find(0,sum_value)
    print(f'#{test_case+1} {min_value}')


