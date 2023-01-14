import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 
title = []
lst = []
for _ in range(N):
    name, score = input().rstrip().split()
    title.append((name, int(score)))

for _ in range(M):
    inp = int(input())
    left, right = 0, N-1
    while left <= right:
        mid = (left+right)//2
        if title[mid][1] >= inp:
            right = mid-1
        elif title[mid][1] < inp:
            left = mid+1
    print(title[left][0])
