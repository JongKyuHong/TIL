import sys
input = sys.stdin.readline

n = int(input())
target = int(input())
res = []
cnt = 0
for _ in range(n-1):
    res.append(int(input()))
res.sort(reverse=True)
if n == 1:
    print(0)
else:
    while 1:
        if res[0] >= target:
            res[0] -= 1
            target += 1
            cnt += 1
            res.sort(reverse=True)
        else:
            print(cnt)
            break
