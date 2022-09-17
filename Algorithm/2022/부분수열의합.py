import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

ans = 0

def find(idx, sum_v):
    global ans
    if idx >= N:
        return
    sum_v += array[idx]
    if sum_v == S:
        ans += 1
        
    find(idx+1, sum_v)
    find(idx+1, sum_v-array[idx])

find(0, 0)
print(ans)