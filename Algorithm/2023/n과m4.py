import sys
input = sys.stdin.readline

def make(arr, length, standard):
    if length == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if i >= standard:
            make(arr+[i], length+1, i)
N, M = map(int, input().split())

for i in range(1, N+1):
    make([i], 1, i)