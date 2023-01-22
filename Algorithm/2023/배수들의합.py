import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = set()
for num in nums:
    for i in range(num, N+1, num):
        result.add(i)
print(sum(result))
