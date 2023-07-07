import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[float('inf')]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1
    lst[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == k or j == k or j == i:
                continue
            lst[i][j] = min(lst[i][k]+lst[k][j], lst[i][j])

target_a, target_b = 0, 0
min_v = float('inf')
for a in range(1, N+1):
    for b in range(1, N+1):
        tmp = 0
        if a == b:
            continue
        for i in range(1, N+1):
            if i == a or i == b:
                continue
            tmp += min(lst[a][i], lst[b][i])
        if min_v > tmp:
            target_a = a
            target_b = b
            min_v = tmp
        elif min_v == tmp:
            if target_a > a:
                target_a = a
                target_b = b
            elif target_a == a:
                if target_b > b:
                    target_a = a
                    target_b = b
                                
if target_a < target_b:
    print(target_a, target_b, min_v*2)
else:
    print(target_b, target_a, min_v*2)
# 경로걸리는 시간은 i-j (i > j)
# a, b 로 주어진 경로는 이어져 있음
