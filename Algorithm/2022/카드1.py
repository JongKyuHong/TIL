import sys
input = sys.stdin.readline

n = int(input())
lst = list(range(1,n+1))
res = []
while len(lst) > 1:
    res.append(lst.pop(0))
    target = lst.pop(0)
    lst.append(target)

res.append(lst[0])
print(*res)