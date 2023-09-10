import sys 
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
lst = defaultdict(int)
for _ in range(N):
    num = int(input())
    lst[num] += 1

for num, cnt in sorted(lst.items(), key=lambda x: x[0]):
    for _ in range(cnt):
        print(num)
