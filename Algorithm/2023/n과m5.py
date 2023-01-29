import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def make(arr, length):
    if length == M:
        print(*arr)
        return
    for i in range(N):
        if lst[i] not in arr:
            make(arr+[lst[i]], length+1)

for i in range(N):
    make([lst[i]], 1)