import sys
input = sys.stdin.readline

N, K = map(int, input().split())
target = 0
for i in range(1, K+1):
    target += i
if N < target:
    print(-1)
else:
    if (N-target) % K == 0:
        print(K-1)
    else:
        print(K)


