import sys
input = sys.stdin.readline

N, T = map(int, input().split())
carrot = []
for i in range(N):
    w, p = map(int, input().split())
    carrot.append((w,p))

carrot.sort(key=lambda x:((x[1]*(T-1))))
ans = 0
for i in range(T, T-N, -1):
    w, p = carrot.pop()
    ans += w + p*(i-1)

print(ans)