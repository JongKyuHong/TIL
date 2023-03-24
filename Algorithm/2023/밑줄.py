import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []
len_ = 0
order = []
for _ in range(N):
    inp = input().rstrip()
    len_ += len(inp)
    words.append(inp)
default_len, r = divmod(M-sum(map(len,words)), N-1)

result = words[0]
for i in range(1, N):
    if words[i][0].islower() and r != 0:
        r -= 1
        result += '_'*(default_len+1)+words[i]
    elif i + r == N:
        r -= 1
        result += '_'*(default_len+1)+words[i]
    else:
        result += '_'*default_len + words[i]
print(result)