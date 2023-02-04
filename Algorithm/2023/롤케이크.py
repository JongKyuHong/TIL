import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort(key=lambda x: (x%10, x))
ans = 0
for i in range(N):
    tmp = cakes[i]//10
    #print(cakes[i], M, ans)
    if cakes[i]%10 == 0:
        if tmp-1 <= M:
            M -= (tmp-1)
            ans += tmp
        else:
            ans += M
            M -= M
    else:
        if tmp > M:
            ans += M
            M -= M
        else:
            M -= tmp
            ans += tmp
print(ans)