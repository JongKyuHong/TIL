import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
nums = list(map(int, input().split()))
nums.append(new)
nums.sort(reverse=True)
idx = nums.index(new)+1
if idx > P:
    print(-1)
else:
    if N == P and new == nums[-1]:
        print(-1)
    else:
        print(idx)
        
