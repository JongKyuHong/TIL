from collections import deque
import sys 
input = sys.stdin.readline

def solve(target):
    # 이제부터 최대중량 target을 옮길수있는지가 중요함
    # 메모리제한이 굉장히 빡빡해서 2차원배열을 사용할 수가 없다. 그래서 어떻게 target이 가능한지 입증하는과정이 좀 어려움
    # target을 기준으로 bfs를 통해 가장 가까운 거리를 찾음?
    q = deque([])
    q.append(p1)
    visited = [0]*N
    visited[p1] = 1
    while q:
        now = q.popleft()
        for b, cost in lst[now]:
            if not visited[b] and cost >= target:
                visited[b] = 1
                q.append(b)
    return visited[p2]

N, M = map(int, input().split())
lst = [[] for _ in range(N)]
start, end = float('inf'), 1
for _ in range(N):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    lst[A].append([B, C])
    lst[B].append([A, C])
    start = min(start, C)
    end = max(end, C)

p1, p2 = map(int, input().split())
p1 -= 1
p2 -= 1
result = start
while start <= end:
    mid = (start+end) // 2
    if solve(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
    
