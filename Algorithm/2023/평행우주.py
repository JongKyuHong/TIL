import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
value = 0
for i in range(n-1, -1, -1):
    if value > lst[i]:
        if value % lst[i]:
            value = (value//lst[i]+1)*lst[i]
    else:
        value = lst[i]
print(value)