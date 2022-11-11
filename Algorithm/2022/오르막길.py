import sys 
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()
prev = lst[0]
deep = 0
start = 1
while 1:
    if prev < lst[start]:
        flag = 0
        start_point = prev
        for i in range(start, n-1):
            if lst[i] < lst[i+1]:
                continue
            else:
                deep = max(lst[i] - start_point, deep)
                start = i
                flag = 1
                break
        if not flag:
            deep = max(lst[n-1]-start_point, deep)
            break
    prev = lst[start]
    start += 1
    if start >= n:
        break
print(deep)
