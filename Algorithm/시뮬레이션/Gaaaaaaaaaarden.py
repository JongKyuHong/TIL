import sys 
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
delta = ((0,1),(1,0),(-1,0),(0,-1))

def arrangement(arr):
    for com in combinations(arr, G):
        greenq = deque()
        redq = deque()
        lst2 = deepcopy(lst)
        for i in range(len(arr)):
            r, c = arr[i]
            if arr[i] in com:
                # greenq
                greenq.append((r, c))
                lst2[r][c] = 3
            else:
                redq.append((r, c))
                lst2[r][c] = 4
        solve(greenq, redq, lst2)

def solve(greenq, redq, lst2):
    global answer
    flowers_count = 0
    while 1:
        green = set()
        red = set()
        while greenq:
            r, c = greenq.popleft()
            for dr, dc in delta:
                nr, nc = dr+r, dc+c
                if 0 <= nr < N and 0 <= nc < M and (lst2[nr][nc] == 1 or lst2[nr][nc] == 2):
                    green.add((nr, nc))

        while redq:
            r, c = redq.popleft()
            for dr, dc in delta:
                nr, nc = dr+r, dc+c
                if 0 <= nr < N and 0 <= nc < M and (lst2[nr][nc] == 1 or lst2[nr][nc] == 2):
                    red.add((nr, nc))

        # 둘중 하나만 비어도 더이상 꽃이 만들어 지지 않기 때문에 볼 필요가 없다.
        if not green or not red:
            answer = max(answer, flowers_count)
            return
        blacklist = set()
        for i, j in green:
            lst2[i][j] = 3

        for i, j in red:
            if lst2[i][j] == 3:
                lst2[i][j] = 5 # 꽃을 피운다.
                blacklist.add((i, j))
                flowers_count += 1
            else:
                lst2[i][j] = 4
                redq.append((i, j))

        for i, j in green:
            if (i, j) not in blacklist:
                greenq.append((i, j))
N, M, G, R = map(int, input().split())

coordinate = []
lst = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j] == 2: # 배양액을 뿌릴 수 있는 공간
            coordinate.append((i, j))

answer = 0
# coordinate에서 G+R개를 뽑아서 배치하자
for com in combinations(coordinate, G+R):
    # 초록색은 3 빨간색은 4
    arrangement(com)
print(answer)