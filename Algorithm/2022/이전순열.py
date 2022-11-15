from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
target = permutations(range(1,n+1), n)
lst = tuple(map(int, input().split()))
idx = 0
prev = []
for t in target:
    if idx == 0:
        if t == lst:
            print(-1)
            exit()
        prev = t
        idx += 1

    if t == lst:
        print(*prev)
        break
    prev = t