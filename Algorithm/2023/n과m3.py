import sys
input = sys.stdin.readline

def make(arr, length):
    if length == M:
        print(*arr)
        return
    for i in range(1, N+1):
        make(arr+[i], length+1)

N, M = map(int, input().split())

for i in range(1, N+1):
    make([i], 1)