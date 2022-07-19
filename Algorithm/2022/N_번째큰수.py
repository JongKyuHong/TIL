import heapq
n = int(input())
q = []
res = 0
for _ in range(n):
    ans = list(map(int, input().split()))
    if not q:
        for a in ans:
            heapq.heappush(q, a)
    else:
        for a in ans:
            print(q, a)
            print(q[0])
            if q[0] < a:
                heapq.heappush(q, a)
                heapq.heappop(q)
print(q[0])