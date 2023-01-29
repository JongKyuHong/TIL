import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
visited = [0]*N
def make(arr, length):
    if length == M:
        print(*arr)
        return
    standard = 0
    for i in range(N):
        if not visited[i] and standard != lst[i]:
            visited[i] = 1
            standard = lst[i]
            make(arr+[lst[i]], length+1)
            visited[i] = 0

make([], 0)