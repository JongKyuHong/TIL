import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
answer = 0
start, end = 0, 1
while end <= len(A):
    target = sum(A[start:end])
    if target == M:
        answer += 1
        start += 1
        end += 1
    elif target < M:
        end += 1
    else:
        start += 1
print(answer)