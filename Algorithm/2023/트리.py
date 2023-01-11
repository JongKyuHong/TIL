from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
child = [[] for _ in range(N)]
root = 0
D = int(input())
for i in range(N):
    if lst[i] != -1:
        if i != D:
            child[lst[i]].append(i)
    else:
        root = i

def bfs():
    if root == D:
        return 0
    q = deque()
    q.append(root)
    visited = [0]*N
    visited[root] = 1
    cnt = 0 
    while q:
        now = q.popleft()
        if not child[now]:
            cnt += 1
        else:
            for i in child[now]:
                if not visited[i] and i != -1:
                    q.append(i)
                    visited[i] = 1
    return cnt
print(bfs())
