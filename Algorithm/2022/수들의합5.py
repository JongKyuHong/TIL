import sys
input = sys.stdin.readline

N = int(input()) # 
S = list(range(1, N+1))

summary = 0
cnt = 0
end = 0
for start in range(N):
    while summary < N and end < N:
        summary += S[end]
        end += 1
    if summary == N:
        cnt += 1
    summary -= S[start]

print(cnt)


