import sys
input = sys.stdin.readline

def maxsize(r, c):
    max_size = 100
    for i in range(100):
        if r+i > 100:
            break
        for j in range(100):
            if c+j > 100:
                break
            max_size = max(max_size, calculate_area(r, c, r+i, c+j))
    return max_size

def calculate_area(r, c, dr, dc):
    cnt = 0
    for i in range(r, dr+1):
        for j in range(c, dc+1):
            if not paper[i][j]:
                return 0
            else:
                cnt += 1
    return cnt

N = int(input())
paper = [[0]*101 for _ in range(101)]
for _ in range(N):
    a, b = map(int, input().split())
    for j in range(b, b+10):
        for i in range(a, a+10):
            paper[j][i] = 1

max_v = 100
flag = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            max_v = max(max_v, maxsize(i, j))
print(max_v)