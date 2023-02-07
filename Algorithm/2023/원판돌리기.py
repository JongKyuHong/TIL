from collections import deque
import sys
input = sys.stdin.readline

def rotate_(x, d, k):
    for _ in range(k):
        for i in range(x, N+1, x):
            if d == 0:
                graph[i-1].rotate(1)
            else:
                graph[i-1].rotate(-1)

def drop_number():
    visited = [[1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M-1):
            if graph[i][j] != 0 and graph[i][j+1] != 0 and graph[i][j] == graph[i][j+1]:
                visited[i][j] = 0
                visited[i][j+1] = 0
        if graph[i][0] != 0 and graph[i][M-1] != 0 and graph[i][0] == graph[i][M-1]:
                visited[i][0] = 0
                visited[i][M-1] = 0

    for i in range(N-1):
        for j in range(M):
            if graph[i][j] != 0 and graph[i+1][j] != 0 and graph[i][j] == graph[i+1][j]:
                visited[i][j] = 0
                visited[i+1][j] = 0
    return visited
N, M, T = map(int, input().split())

graph = [deque(list(map(int, input().split()))) for _ in range(N)]
for _ in range(T):
    x, d, k = map(int, input().split())
    rotate_(x, d, k)
    visited = drop_number()
    flag = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                flag = 1
                graph[i][j] = 0
    if flag == 0:
        sum_v = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0:
                    sum_v += graph[i][j]
                    cnt += 1
        if cnt == 0:
            continue
        avg = sum_v/cnt

        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0:
                    if avg > graph[i][j]:
                        graph[i][j] += 1
                    elif avg < graph[i][j]:
                        graph[i][j] -= 1

ans = 0
for i in graph:
    ans += sum(i)
print(ans)


