# 맥주마심녀서 걸어가기
from collections import deque
delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(r,c,beer):
    q = deque()
    q.append((r,c,beer))
    while q:
        r,c,beer = q.popleft()
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < 

for test_case in range(int(input())):
    n = int(input())
    homex,homey = map(int,input().split())
    city = []
    for _ in range(n):
        city.append(list((map(int, input().split()))))
    fx,fy = map(int, input().split())
