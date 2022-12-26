import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    tmp = [lst.pop()]
    while lst:
        tmp = [lst.pop()] + tmp
        if lst:
            tmp = tmp + [lst.pop()]
    max_v = max(0, abs(tmp[0]-tmp[n-1]))
    for i in range(n-1):
        max_v = max(max_v, abs(tmp[i]-tmp[i+1]))
    print(max_v)