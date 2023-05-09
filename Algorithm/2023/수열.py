import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 0
max_v = -float('inf')
sum_v = 0
cnt = 0
while right < N:
    while cnt < K:
        sum_v += lst[right]
        cnt += 1
        right += 1
    max_v = max(max_v, sum_v)
    sum_v -= lst[left]
    left += 1
    cnt -= 1
print(max_v)

