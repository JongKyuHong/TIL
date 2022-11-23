import sys
input = sys.stdin.readline

c, p = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
if p == 1:
    ans += c
    for i in range(c-3):
        if lst[i] == lst[i + 1] == lst[i + 2] == lst[i + 3]:
            ans+=1
elif p == 2:
    for i in range(c-1):
        if lst[i] == lst[i+1]:
            ans += 1
elif p == 3:
    for i in range(c-2):
        if lst[i] == lst[i+1] == lst[i+2]-1:
            ans += 1
    for i in range(c-1):
        if lst[i] == lst[i+1]+1:
            ans += 1
elif p == 4:
    for i in range(c-2):
        if lst[i]-1 == lst[i+1] == lst[i+2]:
            ans += 1
    for i in range(c-1):
        if lst[i] == lst[i+1]-1:
            ans += 1
elif p == 5:
    for i in range(c-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            ans += 1
    for i in range(c-1):
        if lst[i] == lst[i+1]-1:
            ans += 1
    for i in range(c-2):
        if lst[i]-1 == lst[i+1] == lst[i+2]-1:
            ans += 1
    for i in range(c-1):
        if lst[i]-1 == lst[i+1]:
            ans += 1
elif p == 6:
    for i in range(c-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            ans += 1
    for i in range(c-1):
        if lst[i]-2 == lst[i+1]:
            ans += 1
    for i in range(c-2):
        if lst[i] == lst[i+1]-1 == lst[i+2]-1:
            ans += 1
    for i in range(c-1):
        if lst[i] == lst[i+1]:
            ans += 1
elif p == 7:
    for i in range(c-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            ans += 1
    for i in range(c-1):
        if lst[i] == lst[i+1]:
            ans += 1
    for i in range(c-2):
        if lst[i]-1 == lst[i+1]-1 == lst[i+2]:
            ans += 1
    for i in range(c-1):
        if lst[i] == lst[i+1]-2:
            ans += 1
print(ans)