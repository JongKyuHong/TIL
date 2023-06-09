import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    tmp = lst[i-1:j]
    tmp.reverse()
    lst[i-1:j] = tmp
for i in range(N):
    print(lst[i],end=' ')