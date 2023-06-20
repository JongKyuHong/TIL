import sys
input = sys.stdin.readline

N, M = input().rstrip().split()
lst = [input().rstrip() for _ in range(int(N))]
visited = {}
ans = 0
if M == 'Y':
    cnt = 0
    for i in range(len(lst)):
        if lst[i] not in visited:
            visited[lst[i]] = 1
            cnt += 1
            if cnt == 1:
                cnt = 0
                ans += 1
elif M == 'F':
    cnt = 0
    for i in range(len(lst)):
        if lst[i] not in visited:
            visited[lst[i]] = 1
            cnt += 1
            if cnt == 2:
                cnt = 0
                ans += 1
else: # O
    cnt = 0
    for i in range(len(lst)):
        if lst[i] not in visited:
            visited[lst[i]] = 1
            cnt += 1
            if cnt == 3:
                cnt = 0
                ans += 1
print(ans)