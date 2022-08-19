import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

def dd(idx, v):
    global cnt
    if idx >= n:
        return
    v += nums[idx]
    if v == s:
        cnt += 1
    dd(idx+1, v)
    dd(idx+1, v-nums[idx])

cnt = 0
dd(0, 0)
print(cnt)