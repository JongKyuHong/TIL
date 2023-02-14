import sys
input = sys.stdin.readline

N = int(input())
food = []
ans = float('inf')
for _ in range(N):
    a, b = map(int, input().split())
    food.append((a,b))
    ans = min(ans, abs(a-b))

def dfs(value, s, c, idx):
    global ans
    #print(value, s, c, 'vv')
    ans = min(ans, value)
    if idx == N:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            s1 = s*food[i][0]
            c1 = c+food[i][1]
            dfs(abs(s1-c1), s1, c1, idx+1)
            visited[i] = 0    

visited = [0]*N
dfs(ans, 1, 0, 0)
print(ans)