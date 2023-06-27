import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    d1, d2, d3 = map(int, input().split())
    if d1 == d2 == d3:
        ans = max(ans, 10000+d1*1000)
    elif d1 == d2:
        ans = max(ans, 1000+d1*100)
    elif d2 == d3:
        ans = max(ans, 1000+d2*100)
    elif d1 == d3:
        ans = max(ans, 1000+d1*100)
    else:
        ans = max(ans, max(d1, d2, d3)*100)
print(ans)

