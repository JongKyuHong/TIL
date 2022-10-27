import sys
input = sys.stdin.readline

n, d = map(int, input().split())
answer = 0
A = list(range(1, n+1))
for i in A:
    for j in str(i):
        if int(j) == d:
            answer += 1
print(answer)