import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def make(arr, length, standard):
    if length == M:
        print(*arr)
        return
    for i in range(N):
        if lst[i] >= standard:
            make(arr+[lst[i]], length+1, lst[i])

for i in range(N):
    make([lst[i]], 1, lst[i])