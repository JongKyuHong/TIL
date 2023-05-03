import sys
input = sys.stdin.readline

N = int(input())
days = [0]*366
idx = 0
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        days[i] += 1

ans = 0
cnt = 0
max_v = 0
for i in range(1, 366):
    if days[i]:
        cnt += 1
        max_v = max(max_v, days[i])
    else:
        ans += cnt*max_v
        cnt = 0
        max_v = 0
if cnt:
    ans += cnt*max_v
print(ans)
    
