import sys
input = sys.stdin.readline
n, k = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split())) # Pdi값을 i번째로 가지고 오는것 즉 P1값을 1번째로 가져오는것
res = []

def solve(S, D):
    P = [[0] for _ in range(n)]
    idx = 0
    while 1:
        P[D[idx]-1] = S[idx]
        idx += 1
        if idx % n == 0:
            break
    return P


for i in  range(k):
    if i == 0:
        res = solve(S, D)
    else:
        res = solve(res, D)
print(*res)