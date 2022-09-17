from collections import deque

for T in range(int(input())):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]

    for i in range(0,m*2,2):
        graph[nums[i]].append(nums[i+1])
        graph[nums[i+1]].append(nums[i])
    visited = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            q = deque()
            q.append(i)
            while q:
                v = q.popleft()
                for next_node in graph[v]:
                    if not visited[next_node]:
                        visited[next_node] = 1
                        q.append(next_node)
    print(f'#{T+1} {cnt}')