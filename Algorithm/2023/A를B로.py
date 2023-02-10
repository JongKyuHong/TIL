import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

if sorted(A) != sorted(B):
    print(-1)
    exit()
idx = len(A)-1
if idx == 0:
    if A == B:
        print(0)
    else:
        print(-1)
    exit()
cnt = 0
for i in range(len(A)-1, -1, -1):
    if A[i] != B[idx]:
        cnt += 1
    else:
        idx -= 1
print(cnt)

