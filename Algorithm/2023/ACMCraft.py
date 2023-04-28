from collections import deque
import sys
input = sys.stdin.readline

def find():
    q = deque()
    dp = [0]*(N+1)
    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] += D[i]
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[now] + D[i])
            if in_degree[i] == 0:
                q.append(i)
    return dp[W]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    dp = [0]*(N+1)
    in_degree = [0]*(N+1)
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1
    W = int(input())
    print(find())
# 1. 부모 건물?을 지어야 자식 건물 지을수 있다. 
# 1-2. 찾아야하는 건물번호를 입력했을때, 부모 건물들을 나열할 수 있어야 한다.
# 1-3. 부모가 없을때 순회 멈추면 될듯

# 2. 최소 시간을 알아내야 한다.
# 2-1. 부모의 요소들은 모두 동시에 지을 수 있다. 그 중 시간이 가장 많이 소요되는 건물만 짓는다고 생각하면 될것같다.
