import sys
input = sys.stdin.readline

K, L = map(int, input().split())
min_v = K
for i in range(L-1, 1, -1):
    if K % i == 0:
        min_v = i

if min_v == K:
    print("GOOD")
else:
    print('BAD',min_v)