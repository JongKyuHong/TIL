import sys
input = sys.stdin.readline

def dfs(string):
    if len(string) == len(word):
        print(''.join(string))
        return
    for i in visited: 
        if visited[i]:
            visited[i] -= 1
            dfs(string + i)
            visited[i] += 1

N = int(input())

for _ in range(N):
    word = sorted(map(str, input().rstrip()))
    visited = {}
    for i in word:
        if i not in visited:
            visited[i] = 1
        else:
            visited[i] += 1
    dfs('')