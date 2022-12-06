import sys
input = sys.stdin.readline

n = int(input()) # 전체 용액수
lst = list(map(int, input().split())) # 
lst.sort()
start = 0
end = n-1
res = float('inf')
ans = []
while start < end:
    if res > abs(lst[start] + lst[end]):
        res = abs(lst[start]+lst[end])
        ans = [lst[start], lst[end]]
    if lst[start] + lst[end] < 0:
        start += 1
    else:
        end -= 1
    
print(ans[0], ans[1])