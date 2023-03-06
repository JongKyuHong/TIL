from itertools import combinations
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
ans = 0
cnt_lst = 0
for combi in combinations(range(N), M):
    cnt = 0
    cnt_lst += 1
    for i in range(M):
        if combi[i] < M:
            cnt += 1
    if cnt >= K:
        ans += 1
print(ans/cnt_lst)