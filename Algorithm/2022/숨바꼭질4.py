from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0]*100001
visited[n] = 1
if n > k:
    cnt = 0
    path = [n]
    standard = n
    for i in range(1,n-k+1):
        cnt += 1
        path += [n-i]
    print(cnt)
    print(*path)
    exit()

q = deque([[n, [n], 0]])
while q:
    n, path, second = q.popleft()
    if n == k:
        print(second)
        print(*path)
        exit()
    for i in range(3):
        if i == 2 and n+1 < 100001 and not visited[n+1]:
            visited[n+1] = 1
            q.append((n+1, path+[n+1], second+1))
        elif i == 1 and n-1 >= 0 and not visited[n-1]:
            visited[n-1] = 1
            q.append((n-1, path+[n-1], second+1))
        elif i == 0 and 2*n < 100001 and not visited[2*n]:
            visited[2*n] = 1
            q.append((2*n, path+[2*n], second+1))