import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
n = 0
while bin(N).count('1') > K:
    N += 1
    count += 1
print(count)