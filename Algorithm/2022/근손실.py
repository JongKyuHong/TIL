import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
standard = 500
visited = [0]*n
cnt = 0
def dfs(target, weight):
    if target == n:
        global cnt
        cnt += 1 
    for i in range(n):
        if weight + lst[i] - k >= 500 and not visited[i]:
            visited[i] = 1
            dfs(target+1, weight+lst[i]-k)
            visited[i] = 0
            
for i in range(n):
    if lst[i]-k >= 0:
        visited[i] = 1
        dfs(1, 500+lst[i]-k)
        visited[i] = 0

print(cnt)