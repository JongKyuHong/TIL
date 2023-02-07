import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort(key=lambda x:(abs(x)))
ans = float('inf')
for i in range(N-1):
    value = lst[i]+lst[i+1]
    if abs(value) < abs(ans):
        ans = value
print(ans)