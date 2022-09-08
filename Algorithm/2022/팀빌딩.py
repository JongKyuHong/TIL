import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

#S.sort()
start = 0
end = N-1
max_v = 0
while start < end:
    summary = (end-start-1) * min(S[start], S[end])
    if max_v < summary:
        max_v = summary
        if S[start] > S[end]:
            end -= 1
        else:
            start += 1
    else:
        if S[start] > S[end]:
            end -= 1
        else:
            start += 1
print(max_v)