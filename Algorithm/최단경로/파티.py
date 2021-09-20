import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline

def dij(x):
    d = [INF]*n
    heapq.heappush(heap, [0, x])
    d[x] = 0
    while heap:
        w, x = heapq.heappop(heap)
        for nw, nx in a[x]:
            nw += w
            if nw < d[nx]:
                d[nx] = nw
                heapq.heappush(heap, [nw, nx])
    return d

n, m, t = map(int, input().split())
a = [[]*n for _ in range(n)]
heap = []

for i in range(m):
    x, y, w = map(int, input().split())
    a[x-1].append([w, y-1])

ans = [0]*n
for i in range(n):
    d = dij(i)
    ans[i] += d[t-1]
    d = dij(t-1)
    ans[i] += d[i]
print(max(ans))