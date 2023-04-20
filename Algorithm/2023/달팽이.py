import sys
input = sys.stdin.readline

N = int(input())
nums = int(input())
lst = [[0]*N for _ in range(N)]
dir = 0
lst[0][0] = N**2
q = [[0, 0, N**2]]
ans = []
while q:
    r, c, val = q.pop()
    if val == nums:
        ans = [r, c]
    if dir == 0:
        nr, nc = r+1, c
    elif dir == 1:
        nr, nc = r, c+1
    elif dir == 2:
        nr, nc = r-1, c
    else:
        nr, nc = r, c-1
    if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 0:
        lst[nr][nc] = val-1
        q.append((nr, nc, val-1))
    else:
        if val != 1:
            dir += 1
            dir %= 4
            q.append((r, c, val))
for i in lst:
    print(*i)
print(ans[0]+1, ans[1]+1)