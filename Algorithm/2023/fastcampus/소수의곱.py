import heapq
import sys 
input = sys.stdin.readline

K, N = map(int, input().split())
nums = list(map(int, input().split()))
q = []
for num in nums:
    heapq.heappush(q, num)
visited = set()
max_value = max(nums)
for i in range(N-1):
    out = heapq.heappop(q)
    for num in nums:
        tmp = out * num
        if len(q) >= N and max_value < tmp:
            continue
        if tmp not in visited:
            visited.add(tmp)
            max_value = max(max_value, tmp)
            heapq.heappush(q, tmp)
print(heapq.heappop(q))