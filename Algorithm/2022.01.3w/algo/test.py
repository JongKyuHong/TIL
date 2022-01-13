# 숨바꼭질
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dp = [100000000 for i in range(n + 1)]
    dp[start] = 0
    while heap:
        we, nu = heappop(heap)
        for n_nu, n_we in s[nu]:
            wei = we + n_we
            if dp[n_nu] > wei:
                dp[n_nu] = wei
                heappush(heap, [wei, n_nu])
    return dp
for i in range(m):
    a, b = map(int, input().split())
    s[a].append([b, 1])
    s[b].append([a, 1])
dp = dijkstra(1)
max_dp = max(dp[1:])
print(dp.index(max_dp), max_dp, dp.count(max_dp))