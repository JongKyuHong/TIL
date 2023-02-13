import sys
input = sys.stdin.readline

def dfs(lst, depth):
    global ans
    if depth == N:
        total = 0
        for i in range(N-1):
            total += abs(lst[i]-lst[i+1])
        ans = max(ans, total)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            lst.append(A[i])
            dfs(lst, depth+1)
            visited[i] = 0
            lst.pop()

N = int(input())
A = list(map(int, input().split()))
visited = [0]*N
ans = 0

dfs([], 0)
print(ans)