import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
for idx, value in enumerate(sorted(list(map(int, input().split())))):
    if idx+1 == K:
        print(value)
        break