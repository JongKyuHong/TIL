import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input()) # 카드 장수 1 ~ 99
k = int(input()) # 선택하는 카드 갯수
# 만들수있는 정수의 갯수는?
nums = [input().rstrip() for _ in range(n)]
res = set()
for per in permutations(nums,k):
    res.add(''.join(per))
print(len(res))

