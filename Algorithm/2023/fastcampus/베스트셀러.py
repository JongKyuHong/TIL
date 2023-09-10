import sys 
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    inp = input().rstrip()
    dic[inp] += 1

print(sorted(sorted(dic.items(), key=lambda x: x[0]), key=lambda x:x[1], reverse=True)[0][0])

