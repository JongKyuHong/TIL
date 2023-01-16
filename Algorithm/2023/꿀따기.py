import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 1. 제일 왼쪽꿀통, 벌두마리 오른쪽 둘
S = lst[:]
max_v = 0
for i in range(1, N):
    S[i] += S[i-1]
for i in range(1, N-1):
    max_v = max(max_v, 2*S[-1]-lst[0]-lst[i]-S[i])
for i in range(1, N-1):
    max_v = max(max_v, S[-1]-lst[-1]-lst[i]+S[i-1])
for i in range(1, N-1):
    max_v = max(max_v, S[i]-lst[0]+S[-1]-S[i-1]-lst[-1])
print(max_v)