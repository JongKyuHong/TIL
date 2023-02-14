import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find(idx, depth):
    #print(idx, depth,'idx')
    if depth == 5:
        print(1)
        exit()
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = 1
            find(i, depth+1)
            visited[i] = 0

visited = [0]*N
for i in range(N):
    visited[i] = 1
    find(i, 1)
    visited[i] = 0
print(0)
