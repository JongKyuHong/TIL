from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    house = list(map(int, input().split()))
    store = []
    for _ in range(n):
        data = list(map(int, input().split()))
        store.append(data)
    visited = [0] * len(store)
    rock = list(map(int, input().split()))
    q = deque([(house[0],house[1])])
    flag = 0

    while q:
        r, c = q.popleft()
        if abs(r-rock[0]) + abs(c-rock[1]) <= 1000:
            flag = 1
            break
        for i in range(len(store)):
            if visited[i] == 0:
                if abs(r-store[i][0]) + abs(c-store[i][1]) <= 1000:
                    visited[i] = 1
                    q.append((store[i][0], store[i][1]))
    if flag:
        print('happy')
    else:
        print('sad')

