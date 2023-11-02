import sys 
from collections import defaultdict
input = sys.stdin.readline
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move(r, c, s, d):
    r, c = (r+dr[d]*s)%N, (c+dc[d]*s)%N
    return [r, c]

N, M, K = map(int, input().split())
lst = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1; c -= 1
    lst.append((r, c, m, s, d))

for _ in range(K):
    visited = []
    for r, c, m, s, d in lst:
        r1, c1 = move(r, c, s, d)
        visited.append((r1, c1, m, s, d))

    tmp = defaultdict(list)
    for r, c, m, s, d in visited:
        tmp[(r,c)].append([m, s, d])
        
    lst2 = []
    for key, v in tmp.items():
        i, j = key
        if len(v) >= 2:
            flag = 0
            total_m = 0
            total_s = 0
            for m, s, d in v:
                total_m += m
                total_s += s
                if d % 2:
                    flag += 1
            value = total_m // 5
            speed = total_s // len(v)

            if flag == 0 or flag == len(v):
                if value > 0:
                    lst2.append((i, j, value, speed, 0))
                    lst2.append((i, j, value, speed, 2))
                    lst2.append((i, j, value, speed, 4))
                    lst2.append((i, j, value, speed, 6))
            else:
                if value > 0:
                    lst2.append((i, j, value, speed, 1))
                    lst2.append((i, j, value, speed, 3))
                    lst2.append((i, j, value, speed, 5))
                    lst2.append((i, j, value, speed, 7))
        else:
            m, s, d = v[0]
            if m > 0:
                lst2.append((i, j, m, s, d))
    lst = lst2

answer = 0
for r, c, m, s, d in lst:
    answer += m
print(answer)