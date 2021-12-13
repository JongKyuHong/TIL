from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1
    return answer


def bfs(n, computers, i, visited):
    visited[i] = True
    q = deque()
    q.append(i)
    while q:
        index = q.popleft()
        visited[index] = True
        for a in range(n):
            if computers[index][a] == 1:
                if visited[a] == False:
                    q.append(a)