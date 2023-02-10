from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
S, E = map(int, input().split())

def start_(start, destination):
    q = deque()
    q.append((start,[]))
    lst = []
    while q:
        now, path = q.popleft()
        if now == destination:
            return path
        for i in graph[now]:
            if i not in path:
                q.append((i, path+[i]))

def end_(start, destination, tmp):
    q = deque()
    q.append((start,[]))
    while q:
        now, path = q.popleft()
        if now == destination:
            return path
        for i in graph[now]:
            if i not in path and i not in tmp:
                q.append((i, path+[i]))

path = start_(S, E)
path2 = end_(E, S, path)

print(len(path)+len(path2))