import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jewelry = []
for _ in range(M):
    jewelry.append(int(input()))

jewelry.sort()
left, right = 0, max(jewelry)
ans = float('inf')
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for jew in jewelry:
        q,r = jew//mid, jew%mid
        cnt += jew//mid
        if r > 0:
            cnt += 1
    if cnt > N:
        left = mid+1
    else:
        ans = min(ans, mid)
        right = mid-1   
print(ans)