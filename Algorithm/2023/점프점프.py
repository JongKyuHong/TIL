from collections import deque
n = int(input())
lst = list(map(int, input().split()))
s = int(input())
visited = [0]*n
q = deque()
q.append(s-1)
visited[s-1] = 1
while q:
    now = q.popleft()
    if now-lst[now] >= 0 and not visited[now-lst[now]]:
        visited[now-lst[now]] = 1
        q.append((now-lst[now]))
    if now+lst[now] < n and not visited[now+lst[now]]:
        visited[now+lst[now]] = 1
        q.append((now+lst[now]))
ans = 0
for i in range(n):
    if visited[i]:
        ans += 1
print(ans)


