import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
ans = float('inf')
x,y,z = 1,1,1
while x <= 1001:
    if x not in S:
        y = 1
        while y <= 1001:
            if y not in S:
                z = 1
                while z <= 1001:
                    if z not in S:
                        ans = min(ans, abs(N-(x*y*z)))
                        if N+1 < (x*y*z):
                            break
                    z += 1
            y += 1
    x += 1
print(ans)