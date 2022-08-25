import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]
for _ in range(N):
    a, b, c = map(int, input().split()) # 현재노드, 왼쪽자식노드, 오른쪽자식노드
    graph[a].append((b,c))
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a

def find(node):
    global dist
    for left_node, right_node in graph[node]:
        if left_node != -1 and not visited[left_node]:
            dist += 1
            visited[left_node] = 1
            find(left_node)
        if right_node != -1 and not visited[right_node]:
            dist += 1
            if right_node == N:
                return
            visited[right_node] = 1
            find(right_node)
        if parent[node] :
            dist += 1

dist = 0
visited = [0]*(N+1)
visited[0] = 1
find(1)



print(dist)