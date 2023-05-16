import sys
input = sys.stdin.readline

A, B = map(int, input().split())
lst = [1]*(int(B**0.5)+1)
lst[0], lst[1] = 0, 0
for i in range(2, int(B**0.5)+1):
    if lst[i]:
        if i*i > int(B**0.5):
            break
        for j in range(2*i, int(B**0.5)+1, i):
            lst[j] = 0
ans = 0
for i in range(1, len(lst)):
    if lst[i]:
        res = i*i
        while 1:
            if res < A:
                res *= i
                continue
            if res > B:
                break
            res *= i
            ans += 1
print(ans)