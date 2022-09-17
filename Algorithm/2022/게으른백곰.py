import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 
S = [0] * 1000001
max_len = 0
min_len = sys.maxsize
for _ in range(N):
    g,x = map(int, input().split())
    max_len = max(max_len, x)
    min_len = min(min_len, x)
    S[x] = g

summary = 0
max_v = 0
end = min_len

for start in range(min_len, max_len+1):
    while end < max_len + 1 and end - start <= K*2:
        if S[end] == 0:
            end += 1
            continue
        summary += S[end]
        end += 1
    max_v = max(max_v, summary)
    summary -= S[start]
    
print(max_v)